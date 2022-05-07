# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 12:53:16 2021

@author: Administrator
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 01 유형(DataSet_01.csv 이용)
#
# 구분자 : comma(“,”), 4,572 Rows, 5 Columns, UTF-8 인코딩
# 
# 글로벌 전자제품 제조회사에서 효과적인 마케팅 방법을 찾기
# 위해서 채널별 마케팅 예산과 매출금액과의 관계를 분석하고자
# 한다.
# 컬 럼 / 정 의  /   Type
# TV   /     TV 마케팅 예산 (억원)  /   Double
# Radio / 라디오 마케팅 예산 (억원)  /   Double
# Social_Media / 소셜미디어 마케팅 예산 (억원)  / Double
# Influencer / 인플루언서 마케팅
# (인플루언서의 영향력 크기에 따라 Mega / Macro / Micro / 
# Nano) / String

# SALES / 매출액 / Double
# =============================================================================
# =============================================================================
import pandas as pd

df1 = pd.read_csv('DataSet_01.csv')
df1.head()






#%%

# =============================================================================
# 1. 데이터 세트 내에 총 결측값의 개수는 몇 개인가? (답안 예시) 23
# =============================================================================



df1.isnull().sum().sum()

# 26



#%%

# =============================================================================
# 2. TV, Radio, Social Media 등 세 가지 다른 마케팅 채널의 예산과 매출액과의 상관분석을
# 통하여 각 채널이 매출에 어느 정도 연관이 있는지 알아보고자 한다. 
# - 매출액과 가장 강한 상관관계를 가지고 있는 채널의 상관계수를 소수점 5번째
# 자리에서 반올림하여 소수점 넷째 자리까지 기술하시오. (답안 예시) 0.1234
# =============================================================================



df1[['TV','Radio','Social_Media','Sales']].corr()

# 0.999497





#%%

# =============================================================================
# 3. 매출액을 종속변수, TV, Radio, Social Media의 예산을 독립변수로 하여 회귀분석을
# 수행하였을 때, 세 개의 독립변수의 회귀계수를 큰 것에서부터 작은 것 순으로
# 기술하시오. 
# - 분석 시 결측치가 포함된 행은 제거한 후 진행하며, 회귀계수는 소수점 넷째 자리
# 이하는 버리고 소수점 셋째 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================


# 시험에서 많이 사용되는 패키지 종류 : pandas ,sklearn, statsmodels, scipy, numpy(편의상)

# (1)


df1=df1.dropna()

from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols
from statsmodels.api import OLS, add_constant


x_var = ['TV','Radio','Social_Media']


lm1 = LinearRegression(fit_intercept=True)
lm1.fit(df1[x_var], df1.Sales)

dir(lm1)

lm1.intercept_
lm1.coef_


# (2) 방법2

x = df1[x_var]
xx= add_constant(x)


# 상수항이 안들어가는 버전
lm3=OLS(df1.Sales,x).fit()
lm4=OLS(df1.Sales,xx).fit()





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


#%%

# =============================================================================
# 1.해당 데이터에 대한 EDA를 수행하고, 여성으로 혈압이 High, Cholesterol이 Normal인
# 환자의 전체에 대비한 비율이 얼마인지 소수점 네 번째 자리에서 반올림하여 소수점 셋째
# 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================



df_2 = pd.read_csv('DataSet_02.csv')
df_2


pd.crosstab(index=[df_2.Sex,df_2.BP], columns=df_2.Cholesterol, normalize=True)




























# pd.crosstab(index=[df2.Sex,df2.BP],columns=df2.Cholesterol,normalize=True)


# #crosstab(): 확률 포함, pivot_table(): 별도 연산 필요  
# # 0.105





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

df2 = pd.read_csv('DataSet_02.csv')

import numpy as np

df2['Age_gr'] = np.where(df2.Age<20,'10',
                         np.where(df2.Age<30,'20',
                         np.where(df2.Age<40,'30',
                         np.where(df2.Age<50,'40',
                         np.where(df2.Age<60,'50','60'
                    
    )))))

df2

df2['Na_K_gr'] = np.where(df2.Na_to_K<=10,'Lv1',
                          np.where(df2.Na_to_K<=20,'Lv2',
                                   np.where(df2.Na_to_K<=30,'Lv3','Lv4')))


from scipy.stats import chi2_contingency

temp =pd.crosstab(index=df_2.Sex, columns=df_2.Drug)
temp


out = chi2_contingency(temp)[1]
out

df2.columns
var_list=['Sex', 'BP', 'Cholesterol','Age_gr','Na_K_gr']


out2=[]
for i in var_list:
    temp=pd.crosstab(index=df2[i], columns=df2.Drug)
    out= chi2_contingency(temp)[1]
    out2+=out2+[[i,out]]
    
out3 = pd.DataFrame(out2, columns=['var','pvalue'])
out3.pvalue

out4=out3[out3.pvalue <0.05]
out4['pvalue'].nlargest(1)


# age가 20미만은 '10', 20부터 30 미만은 '20', 30부터 40 미만은
# '30', 40부터 50 미만은 '40', 50부터 60미만은 '50', 60이상은 '60'으로 변환



# 리턴결과 : 지정한 대로 리턴



q2

# Sex ,BP, Cholestreol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지 독립성 검정을 수행하시오.
# - 검정 수행 결과, Drug 타입과 연관성이 있는 변수는 몇 개 인가?





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



import pandas as pd
import numpy as np


df = pd.read_csv('DataSet_02.csv')

df['Sex_cd'] = np.where(df.Sex == 'M', '0','1')
df['BP_cd'] = np.where(df.BP == 'LOW','0',
                       np.where(df.BP =='NORMAL','1','2'))

df['Ch_cd'] = np.where(df.Cholesterol =='NORMAL','0','1')
 

df.head()

x_var = ['Age', 'Na_to_K', 'Ch_cd', 'Sex_cd',
       'BP_cd']

from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text


dt = DecisionTreeClassifier().fit(df[x_var],df.Drug)
dt


plot_tree(dt, max_depth=2, feature_names=x_var,
          class_names=df.Drug.unique())

export_text(dt, feature_names=x_var,decimals=5) # 다섯째 자리까지.

# 14.82850



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


df = pd.read_csv('DataSet_03.csv')
df.head()






#%%

# =============================================================================
# 1.이마의 폭(forehead_width_cm)과 높이(forehead_height_cm) 사이의
# 비율(forehead_ratio)에 대해서 평균으로부터 3 표준편차 밖의 경우를 이상치로
# 정의할 때, 이상치에 해당하는 데이터는 몇 개인가? (답안 예시) 10
# =============================================================================


df.columns

df['forehead_ratio']=df['forehead_width_cm']/df['forehead_height_cm']
df.head()

UU=df['forehead_ratio'].mean()
DD=df['forehead_ratio'].std()


a1=UU-DD*3
a2=UU+DD*3

len(df[(df['forehead_ratio']<a1) | (df['forehead_ratio']>a2)])





#%%

# =============================================================================
# 2.성별에 따라 forehead_ratio 평균에 차이가 있는지 적절한 통계 검정을 수행하시오.
# - 검정은 이분산을 가정하고 수행한다.
# - 검정통계량의 추정치는 절대값을 취한 후 소수점 셋째 자리까지 반올림하여
# 기술하시오.
# - 신뢰수준 99%에서 양측 검정을 수행하고 결과는 귀무가설 기각의 경우 Y로, 그렇지
# 않을 경우 N으로 답하시오. (답안 예시) 1.234, Y
# =============================================================================


#1. 두 집단 차이검정, 수치형 데이터에 대한 평균 차이 검정 : ttest
#2. 이분산/ 등분산 -> 등분산 검정 키워드가 있을 시 독립인 이표본 ttest
#3. 신뢰수준 99% -> 유의수준 0.01로 의사결정을 하라는 의미


df.head()

m1=df[df['gender']=='Male']['forehead_ratio']
f1=df[df['gender']=='Female']['forehead_ratio']

from scipy.stats import ttest_1samp, bartlett, ttest_ind

bartlett(m1,f1) # 대립가설 O, 0.5보다 작다. 이분산

df_out=ttest_ind(m1,f1,equal_var=False)
df_out.pvalue


dir(df_out)

df_out.statistic
abs(df_out.statistic)

# 2.9994984197511543

#%%

# =============================================================================
# 3.주어진 데이터를 사용하여 성별을 구분할 수 있는지 로지스틱 회귀분석을 적용하여
# 알아 보고자 한다. 
# - 데이터를 7대 3으로 나누어 각각 Train과 Test set로 사용한다. 이 때 seed는 123으로
# 한다.
# - 원 데이터에 있는 7개의 변수만 Feature로 사용하고 gender를 label로 사용한다.
# (forehead_ratio는 사용하지 않음)
# - 로지스틱 회귀분석 예측 함수와 Test dataset를 사용하여 예측을 수행하고 정확도를
# 평가한다. 이 때 임계값은 0.5를 사용한다. 
# - Male의 Precision 값을 소수점 둘째 자리까지 반올림하여 기술하시오. (답안 예시) 
# 0.12
# 
# 
# (참고) 
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# train_test_split 의 random_state = 123
# =============================================================================





from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

df=pd.read_csv('DataSet_03.csv')
df.head()


train,test=train_test_split(df,test_size=0.3,random_state=123)


x_var=df.columns.drop('gender')

logit=LogisticRegression()
logit.fit(train[x_var],train.gender)

logit.predict(test[x_var])
logit.predict_proba(test[x_var])


# 성능평가

from sklearn.metrics import classification_report, precision_score

pred=logit.predict(test[x_var])
print(classification_report(test.gender, pred))
precision_score(test.gender, pred, pos_label='Male')
