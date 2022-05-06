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




#%%

# =============================================================================
# 1. 데이터 세트 내에 총 결측값의 개수는 몇 개인가? (답안 예시) 23
# =============================================================================


import pandas as pd 

dataset1 = pd.read_csv('Dataset_01.csv')
dataset1.info()

dataset1.isna().sum()  # 칼럼별 결측치 수
dataset1.isna().sum().sum() # 총 결측치 수 

dataset1.isna().any(axis=1).sum()
# 결측치가 포함된 행의 수

# 정답은 26

#%%

# =============================================================================
# 2. TV, Radio, Social Media 등 세 가지 다른 마케팅 채널의 예산과 매출액과의 상관분석을
# 통하여 각 채널이 매출에 어느 정도 연관이 있는지 알아보고자 한다. 
# - 매출액과 가장 강한 상관관계를 가지고 있는 채널의 상관계수를 소수점 5번째
# 자리에서 반올림하여 소수점 넷째 자리까지 기술하시오. (답안 예시) 0.1234
# =============================================================================


q2=dataset1[['TV','Radio','Social_Media','Sales']].corr()
q2['Sales'].abs().nlargest(2)[1]

q2['Sales'].abs().sort_values(ascending=False)

#정답 : TV 0.999497
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

q3 = dataset1.dropna()

x_var = ['TV','Radio','Social_Media']

from sklearn.linear_model import LinearRegression # 절편 포함
from statsmodels.formula.api import ols #  절편포함
from statsmodels.api import OLS, add_constant # 절편 미포함(절편 추가해야 함.)

lm1 = LinearRegression(fit_intercept=True)
lm1.fit(q3[x_var], q3.Sales)

dir(lm1)

lm1.intercept_ #절편
lm1.coef_ #회귀계수

# (2)
# ols 사용법

form = 'Sales~'+'+'.join(x_var)
lm2=ols(form, data=q3).fit()

lm2.summary()


# (3)

x=q3[x_var]
xx=add_constant(x)


# 상수항 안 들어가는 버전 
lm3=OLS(q3.Sales,x).fit()
lm3.summary()

# 상수항 들어가는 버
lm4=OLS(q3.Sales,xx).fit()
lm4.summary()
