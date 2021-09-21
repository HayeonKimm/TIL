#%%

# =============================================================================
# =============================================================================
# # 문제 02 유형(DataSet_02.csv 이용)
# 구분자 : comma(“,”), 200 Rows, 6 Columns, UTF-8 인코딩

# 환자의 상태와 그에 따라 처방된 약에 대한 정보를 분석하고자한다
# 
# 컬 럼 / 정 의  / Type
# Age  / 연령 / Integer
# Sex / 성별 / String
# BP / 혈압 레벨 / String
# Cholesterol / 콜레스테롤 레벨 /  String
# Na_to_k / 혈액 내 칼륨에 대비한 나트륨 비율 / Double
# Drug / Drug Type / String
# =============================================================================
# =============================================================================


import pandas as pd
data2 = pd.read_csv('Dataset_02.csv')
data2.info()
data2.shape
#%%

# =============================================================================
# 1.해당 데이터에 대한 EDA를 수행하고, 여성으로 혈압이 High, Cholesterol이 Normal인
# 환자의 전체에 대비한 비율이 얼마인지 소수점 네 번째 자리에서 반올림하여 소수점 셋째
# 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================


#crosstab(): 확률 포함, pivot_table(): 별도 연산 필요  

data2.columns
q1 = pd.crosstab(index=[data2.Sex,data2.BP],
                 columns=data2.Cholesterol,
                 normalize=True)

print(q1)




#%%

# =============================================================================
# 2. Age, Sex, BP, Cholesterol 및 Na_to_k 값이 Drug 타입에 영향을 미치는지 확인하기
# 위하여 아래와 같이 데이터를 변환하고 분석을 수행하시오. 
# - Age_gr 컬럼을 만들고, Age가 20 미만은 ‘10’, 20부터 30 미만은 ‘20’, 30부터 40 미만은
# ‘30’, 40부터 50 미만은 ‘40’, 50부터 60 미만은 ‘50’, 60이상은 ‘60’으로 변환하시오. 
# - Na_K_gr 컬럼을 만들고 Na_to_k 값이 10이하는 ‘Lv1’, 20이하는 ‘Lv2’, 30이하는 ‘Lv3’, 30 
# 초과는 ‘Lv4’로 변환하시오.
# - Sex, BP, Cholesterol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지 독립성 검정을
# 수행하시오.
# - 검정 수행 결과, Drug 타입과 연관성이 있는 변수는 몇 개인가? 연관성이 있는 변수
# 가운데 가장 큰 p-value를 찾아 소수점 여섯 번째 자리 이하는 버리고 소수점 다섯
# 번째 자리까지 기술하시오.
# (답안 예시) 3, 1.23456
# =============================================================================

# (1) 변수 생성

q2 = data2.copy()

import numpy as np

# age가 20미만은 '10', 20부터 30 미만은 '20', 30부터 40 미만은
# '30', 40부터 50 미만은 '40', 50부터 60미만은 '50', 60이상은 '60'으로 변환

q2['Age_gr'] = np.where(q2.Age < 20, '10',
                        np.where(q2.Age<30, '20',
                                 np.where(q2.Age<40, '30',
                                          np.where(q2.Age<50, '40',
                                                   np.where(q2.Age<60,'50','60')))))

# 리턴결과 : 지정한 대로 리턴


q2.columns
q2['Na_K_gr'] = np.where(q2.Na_to_K <= 10, 'Lv1',
                         np.where(q2.Na_to_K <= 20,'Lv2',
                                  np.where(q2.Na_to_K <= 30, 'Lv3','Lv4')))

q2

# Sex ,BP, Cholestreol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지 독립성 검정을 수행하시오.
# - 검정 수행 결과, Drug 타입과 연관성이 있는 변수는 몇 개 인가?

from scipy.stats import chi2_contingency

temp = pd.crosstab(index=q2.Sex, columns = q2.Drug)

out = chi2_contingency(temp)[1]

var_list=['Sex','BP','Cholesterol','Age_gr','Na_K_gr']

out2=[]

for i in var_list:
    temp=pd.crosstab(index=q2[i], columns=q2.Drug)
    out=chi2_contingency(temp)[1]
    out2=out2+[[i,out]]
    
out3 = pd.DataFrame(out2, columns=['var','pvalue'])
out4 = out3[out3.pvalue < 0.05]

out4

# out4.sort_values(by='pvalue', ascending=False)[3]
out4['pvalue'].nlargest(1)

# 정답 :4 , 0.000701



#%%

# =============================================================================
# 3.Sex, BP, Cholesterol 등 세 개의 변수를 다음과 같이 변환하고 의사결정나무를 이용한
# 분석을 수행하시오.
# - Sex는 M을 0, F를 1로 변환하여 Sex_cd 변수 생성
# - BP는 LOW는 0, NORMAL은 1 그리고 HIGH는 2로 변환하여 BP_cd 변수 생성
# - Cholesterol은 NORMAL은 0, HIGH는 1로 변환하여 Ch_cd 생성
# - Age, Na_to_k, Sex_cd, BP_cd, Ch_cd를 Feature로, Drug을 Label로 하여 의사결정나무를
# 수행하고 Root Node의 split feature와 split value를 기술하시오. 
# 이 때 split value는 소수점 셋째 자리까지 반올림하여 기술하시오. (답안 예시) Age, 
# 12.345 
# =============================================================================


q3 = data2.copy()

q3['Sex_cd'] = np.where(q3.Sex == 'M',0,1)
q3.BP.unique()

q3['BP_cd'] = np.where(q3.BP =='LOW',0,
                       np.where(q3.BP == 'NORMAL',1,2))

q3['Ch_cd'] = np.where(q3.Cholesterol == 'NORMAL' ,0 ,1)


x_var = ['Age','Na_to_K','Sex_cd','BP_cd','Ch_cd']

from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

dt = DecisionTreeClassifier().fit(q3[x_var],q3.Drug)

dir(dt)

plot_tree(dt,
          max_depth=2,
          feature_names =x_var,
          class_names=q3.Drug.unique())

export_text(dt, feature_names=x_var, decimals=5)

# 정답 : 14.82850










#%%

# =============================================================================
# =============================================================================
# # 문제 03 유형(DataSet_03.csv 이용)
# 
# 구분자 : comma(“,”), 5,001 Rows, 8 Columns, UTF-8 인코딩
# 안경 체인을 운영하고 있는 한 회사에서 고객 사진을 바탕으로 안경의 사이즈를
# 맞춤 제작하는 비즈니스를 기획하고 있다. 우선 데이터만으로 고객의 성별을
# 파악하는 것이 가능할 지를 연구하고자 한다.
#
# 컬 럼 / 정 의 / Type
# long_hair / 머리카락 길이 (0 – 길지 않은 경우 / 1 – 긴
# 경우) / Integer
# forehead_width_cm / 이마의 폭 (cm) / Double
# forehead_height_cm / 이마의 높이 (cm) / Double
# nose_wide / 코의 넓이 (0 – 넓지 않은 경우 / 1 – 넓은 경우) / Integer
# nose_long / 코의 길이 (0 – 길지 않은 경우 / 1 – 긴 경우) / Integer
# lips_thin / 입술이 얇은지 여부 0 – 얇지 않은 경우 / 1 –
# 얇은 경우) / Integer
# distance_nose_to_lip_long / 인중의 길이(0 – 인중이 짧은 경우 / 1 – 인중이
# 긴 경우) / Integer
# gender / 성별 (Female / Male) / String
# =============================================================================
# =============================================================================


import pandas as pd

data3 = pd.read_csv('Dataset_03.csv')



#%%

# =============================================================================
# 1.이마의 폭(forehead_width_cm)과 높이(forehead_height_cm) 사이의
# 비율(forehead_ratio)에 대해서 평균으로부터 3 표준편차 밖의 경우를 이상치로
# 정의할 때, 이상치에 해당하는 데이터는 몇 개인가? (답안 예시) 10
# =============================================================================


q1=data3.copy()

q1['forehead_ratio'] = q1['forehead_width_cm']/q1['forehead_height_cm']

q1

mu = q1['forehead_ratio'].mean()
std = q1['forehead_ratio'].std()

LL = mu -(3*std)
UU = mu +(3*std)


len(q1[(q1['forehead_ratio']<LL) | (q1['forehead_ratio']>UU)])

# 상한하한 둘다 고려해야함.  
        
