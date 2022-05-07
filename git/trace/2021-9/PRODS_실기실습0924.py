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
