# practice - 4
### 실습일
- 210624-2


```python
import pandas as pd
import numpy as np
import seaborn as sns
```


```python
import matplotlib.pyplot as plt
plt.rc('font',family= 'Malgun Gothic')  # 한글깨짐방지 두줄.
plt.rc('axes',unicode_minus=False)


# 그래프가 노트북 안에 보이게 하기 위해
%matplotlib inline
```


```python
from IPython.display import set_matplotlib_formats

set_matplotlib_formats('retina')
```


```python
df=pd.read_csv("소상공인시장진흥공단_상가업소정보_의료기관_201909.csv",low_memory=False)
df.shape
# low_memory는 mixed types를 방지하기위해
```




    (91335, 39)




```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>지점명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>표준산업분류코드</th>
      <th>...</th>
      <th>건물관리번호</th>
      <th>건물명</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>동정보</th>
      <th>층정보</th>
      <th>호정보</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19956873</td>
      <td>하나산부인과</td>
      <td>NaN</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B10</td>
      <td>산부인과</td>
      <td>Q86201</td>
      <td>...</td>
      <td>4127310900110810000010857</td>
      <td>산호한양아파트</td>
      <td>경기도 안산시 단원구 달미로 10</td>
      <td>425764.0</td>
      <td>15236.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>126.814295</td>
      <td>37.336344</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20024149</td>
      <td>타워광명내과의원</td>
      <td>NaN</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B07</td>
      <td>내과/외과</td>
      <td>Q86201</td>
      <td>...</td>
      <td>1168011800104670014000001</td>
      <td>NaN</td>
      <td>서울특별시 강남구 언주로30길 39</td>
      <td>135270.0</td>
      <td>6292.0</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>127.053198</td>
      <td>37.488742</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20152277</td>
      <td>조정현신경외과의원</td>
      <td>NaN</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B15</td>
      <td>신경외과</td>
      <td>Q86201</td>
      <td>...</td>
      <td>4139013200117400001017064</td>
      <td>한라프라자</td>
      <td>경기도 시흥시 중심상가로 178</td>
      <td>429450.0</td>
      <td>15066.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>126.734841</td>
      <td>37.344955</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20350610</td>
      <td>한귀원정신과의원</td>
      <td>NaN</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B99</td>
      <td>기타병원</td>
      <td>NaN</td>
      <td>...</td>
      <td>2650010400100740001009932</td>
      <td>NaN</td>
      <td>부산광역시 수영구 수영로 688</td>
      <td>613100.0</td>
      <td>48266.0</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>129.115438</td>
      <td>35.166872</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20364049</td>
      <td>더블유스토어수지점</td>
      <td>수지점</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>G47811</td>
      <td>...</td>
      <td>4146510100107120002026238</td>
      <td>NaN</td>
      <td>경기도 용인시 수지구 문정로 32</td>
      <td>448170.0</td>
      <td>16837.0</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>127.095522</td>
      <td>37.323528</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 39 columns</p>
</div>



# 결측치


```python
#결측치 세어주기 #결측치:Null,NaN. 데이터가 없는 것.
df.isnull().sum()
```




    상가업소번호           0
    상호명              0
    지점명          89989
    상권업종대분류코드        0
    상권업종대분류명         0
    상권업종중분류코드        0
    상권업종중분류명         0
    상권업종소분류코드        0
    상권업종소분류명         0
    표준산업분류코드      4922
    표준산업분류명       4922
    시도코드           379
    시도명            379
    시군구코드          379
    시군구명           379
    행정동코드            0
    행정동명           379
    법정동코드           55
    법정동명            55
    지번코드             0
    대지구분코드           0
    대지구분명            0
    지번본번지            0
    지번부번지        19256
    지번주소             0
    도로명코드            0
    도로명              0
    건물본번지            0
    건물부번지        80731
    건물관리번호           0
    건물명          44882
    도로명주소            0
    구우편번호           12
    신우편번호            2
    동정보          83929
    층정보          47291
    호정보          75784
    경도               0
    위도               0
    dtype: int64




```python
null_count=df.isnull().sum()
```


```python
null_count.plot.barh(figsize=(5,7))
# figsize로 그래프크기 조율해주기. 글씨크기 때문에
```




    <AxesSubplot:>




    
![png](output_9_1.png)
    



```python
null_count.reset_index()
#reset_index()는 데이터형태로 변환
df_null_count = null_count.reset_index()
```


```python
df_null_count.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>상가업소번호</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>상호명</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>지점명</td>
      <td>89989</td>
    </tr>
    <tr>
      <th>3</th>
      <td>상권업종대분류코드</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>상권업종대분류명</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## 컬럼명 변경하기


```python
df_null_count.columns = ["컬럼명","결측치수"]
df_null_count.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>컬럼명</th>
      <th>결측치수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>상가업소번호</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>상호명</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>지점명</td>
      <td>89989</td>
    </tr>
    <tr>
      <th>3</th>
      <td>상권업종대분류코드</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>상권업종대분류명</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## 정렬하기


```python
df_null_count_top=df_null_count.sort_values(by='결측치수', ascending=False).head(10)

#ascending=False 내림차순으로 value정리
```


```python
df["지점명"] #NAN = 결측치
```




    0         NaN
    1         NaN
    2         NaN
    3         NaN
    4         수지점
             ... 
    91330     베스트
    91331    봄산후조
    91332     NaN
    91333     NaN
    91334     NaN
    Name: 지점명, Length: 91335, dtype: object




```python
df_null_count['컬럼명']
```




    0        상가업소번호
    1           상호명
    2           지점명
    3     상권업종대분류코드
    4      상권업종대분류명
    5     상권업종중분류코드
    6      상권업종중분류명
    7     상권업종소분류코드
    8      상권업종소분류명
    9      표준산업분류코드
    10      표준산업분류명
    11         시도코드
    12          시도명
    13        시군구코드
    14         시군구명
    15        행정동코드
    16         행정동명
    17        법정동코드
    18         법정동명
    19         지번코드
    20       대지구분코드
    21        대지구분명
    22        지번본번지
    23        지번부번지
    24         지번주소
    25        도로명코드
    26          도로명
    27        건물본번지
    28        건물부번지
    29       건물관리번호
    30          건물명
    31        도로명주소
    32        구우편번호
    33        신우편번호
    34          동정보
    35          층정보
    36          호정보
    37           경도
    38           위도
    Name: 컬럼명, dtype: object




```python
drop_columns=df_null_count_top['컬럼명'].tolist() #tolist: 리스트로 바꿔주는함수
drop_columns
```




    ['지점명',
     '동정보',
     '건물부번지',
     '호정보',
     '층정보',
     '건물명',
     '지번부번지',
     '표준산업분류코드',
     '표준산업분류명',
     '시도코드']




```python
df[drop_columns].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지점명</th>
      <th>동정보</th>
      <th>건물부번지</th>
      <th>호정보</th>
      <th>층정보</th>
      <th>건물명</th>
      <th>지번부번지</th>
      <th>표준산업분류코드</th>
      <th>표준산업분류명</th>
      <th>시도코드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>산호한양아파트</td>
      <td>NaN</td>
      <td>Q86201</td>
      <td>일반 의원</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>Q86201</td>
      <td>일반 의원</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>한라프라자</td>
      <td>1.0</td>
      <td>Q86201</td>
      <td>일반 의원</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>수지점</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>G47811</td>
      <td>의약품 및 의료용품 소매업</td>
      <td>41.0</td>
    </tr>
  </tbody>
</table>
</div>



## 결측치 제거하기


```python
print(df.shape)
df=df.drop(drop_columns, axis=1) #1은 열, 0은 행. 값은 재할당해야 반영된다.
print(df.shape)
```

    (91335, 39)
    (91335, 29)
    

## 결과보기


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 91335 entries, 0 to 91334
    Data columns (total 29 columns):
     #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
     0   상가업소번호     91335 non-null  int64  
     1   상호명        91335 non-null  object 
     2   상권업종대분류코드  91335 non-null  object 
     3   상권업종대분류명   91335 non-null  object 
     4   상권업종중분류코드  91335 non-null  object 
     5   상권업종중분류명   91335 non-null  object 
     6   상권업종소분류코드  91335 non-null  object 
     7   상권업종소분류명   91335 non-null  object 
     8   시도명        90956 non-null  object 
     9   시군구코드      90956 non-null  float64
     10  시군구명       90956 non-null  object 
     11  행정동코드      91335 non-null  int64  
     12  행정동명       90956 non-null  object 
     13  법정동코드      91280 non-null  float64
     14  법정동명       91280 non-null  object 
     15  지번코드       91335 non-null  int64  
     16  대지구분코드     91335 non-null  int64  
     17  대지구분명      91335 non-null  object 
     18  지번본번지      91335 non-null  int64  
     19  지번주소       91335 non-null  object 
     20  도로명코드      91335 non-null  int64  
     21  도로명        91335 non-null  object 
     22  건물본번지      91335 non-null  int64  
     23  건물관리번호     91335 non-null  object 
     24  도로명주소      91335 non-null  object 
     25  구우편번호      91323 non-null  float64
     26  신우편번호      91333 non-null  float64
     27  경도         91335 non-null  float64
     28  위도         91335 non-null  float64
    dtypes: float64(6), int64(7), object(16)
    memory usage: 20.2+ MB
    

## 기초통계수치


```python
df.dtypes
```




    상가업소번호         int64
    상호명           object
    상권업종대분류코드     object
    상권업종대분류명      object
    상권업종중분류코드     object
    상권업종중분류명      object
    상권업종소분류코드     object
    상권업종소분류명      object
    시도명           object
    시군구코드        float64
    시군구명          object
    행정동코드          int64
    행정동명          object
    법정동코드        float64
    법정동명          object
    지번코드           int64
    대지구분코드         int64
    대지구분명         object
    지번본번지          int64
    지번주소          object
    도로명코드          int64
    도로명           object
    건물본번지          int64
    건물관리번호        object
    도로명주소         object
    구우편번호        float64
    신우편번호        float64
    경도           float64
    위도           float64
    dtype: object




```python
df['위도'].mean() #mean은 평균
```




    36.62471119236673




```python
df['위도'].median # 중앙값
```




    <bound method NDFrame._add_numeric_operations.<locals>.median of 0        37.336344
    1        37.488742
    2        37.344955
    3        35.166872
    4        37.323528
               ...    
    91330    36.352728
    91331    37.627530
    91332    35.227138
    91333    37.540993
    91334    36.806640
    Name: 위도, Length: 91335, dtype: float64>




```python
df['위도'].max
```




    <bound method NDFrame._add_numeric_operations.<locals>.max of 0        37.336344
    1        37.488742
    2        37.344955
    3        35.166872
    4        37.323528
               ...    
    91330    36.352728
    91331    37.627530
    91332    35.227138
    91333    37.540993
    91334    36.806640
    Name: 위도, Length: 91335, dtype: float64>




```python
df['위도'].min()
```




    33.2192896688307




```python
df['위도'].count()
```




    91335




```python
df['위도'].describe() #통계값 요약
```




    count    91335.000000
    mean        36.624711
    std          1.041361
    min         33.219290
    25%         35.811830
    50%         37.234652
    75%         37.507463
    max         38.499659
    Name: 위도, dtype: float64




```python
df[['위도','경도']].describe() #두개이상은 항상 리스트 한번더
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>위도</th>
      <th>경도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>91335.000000</td>
      <td>91335.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>36.624711</td>
      <td>127.487524</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.041361</td>
      <td>0.842877</td>
    </tr>
    <tr>
      <th>min</th>
      <td>33.219290</td>
      <td>124.717632</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>35.811830</td>
      <td>126.914297</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>37.234652</td>
      <td>127.084550</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>37.507463</td>
      <td>128.108919</td>
    </tr>
    <tr>
      <th>max</th>
      <td>38.499659</td>
      <td>130.909912</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe(include="all") #숫자형으로 출력
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>...</th>
      <th>지번주소</th>
      <th>도로명코드</th>
      <th>도로명</th>
      <th>건물본번지</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>9.133500e+04</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>90956</td>
      <td>90956.000000</td>
      <td>...</td>
      <td>91335</td>
      <td>9.133500e+04</td>
      <td>91335</td>
      <td>91335.000000</td>
      <td>91335</td>
      <td>91335</td>
      <td>91323.000000</td>
      <td>91333.00000</td>
      <td>91335.000000</td>
      <td>91335.000000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>56910</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>34</td>
      <td>34</td>
      <td>17</td>
      <td>NaN</td>
      <td>...</td>
      <td>53118</td>
      <td>NaN</td>
      <td>16610</td>
      <td>NaN</td>
      <td>54142</td>
      <td>54031</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>리원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>경기도</td>
      <td>NaN</td>
      <td>...</td>
      <td>서울특별시 동대문구 제기동 965-1</td>
      <td>NaN</td>
      <td>서울특별시 강남구 강남대로</td>
      <td>NaN</td>
      <td>1123010300109650001031604</td>
      <td>서울특별시 동대문구 약령중앙로8길 10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>152</td>
      <td>91335</td>
      <td>91335</td>
      <td>60774</td>
      <td>60774</td>
      <td>18964</td>
      <td>18964</td>
      <td>21374</td>
      <td>NaN</td>
      <td>...</td>
      <td>198</td>
      <td>NaN</td>
      <td>326</td>
      <td>NaN</td>
      <td>198</td>
      <td>198</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2.121818e+07</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32898.381877</td>
      <td>...</td>
      <td>NaN</td>
      <td>3.293207e+11</td>
      <td>NaN</td>
      <td>251.200482</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>428432.911085</td>
      <td>28085.47698</td>
      <td>127.487524</td>
      <td>36.624711</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.042828e+06</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12985.393171</td>
      <td>...</td>
      <td>NaN</td>
      <td>1.297391e+11</td>
      <td>NaN</td>
      <td>477.456487</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>193292.339066</td>
      <td>18909.01455</td>
      <td>0.842877</td>
      <td>1.041361</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.901108e+06</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>11110.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>1.111020e+11</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100011.000000</td>
      <td>1000.00000</td>
      <td>124.717632</td>
      <td>33.219290</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.001931e+07</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>26350.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>2.635042e+11</td>
      <td>NaN</td>
      <td>29.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>302120.000000</td>
      <td>11681.00000</td>
      <td>126.914297</td>
      <td>35.811830</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.211900e+07</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41117.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>4.111743e+11</td>
      <td>NaN</td>
      <td>92.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>440300.000000</td>
      <td>24353.00000</td>
      <td>127.084550</td>
      <td>37.234652</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.480984e+07</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43113.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>4.311332e+11</td>
      <td>NaN</td>
      <td>257.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>602811.000000</td>
      <td>46044.00000</td>
      <td>128.108919</td>
      <td>37.507463</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.852470e+07</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>50130.000000</td>
      <td>...</td>
      <td>NaN</td>
      <td>5.013049e+11</td>
      <td>NaN</td>
      <td>8795.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>799801.000000</td>
      <td>63643.00000</td>
      <td>130.909912</td>
      <td>38.499659</td>
    </tr>
  </tbody>
</table>
<p>11 rows × 29 columns</p>
</div>




```python
df.describe(include="object") #문자열로 데이터타입으로 출력
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구명</th>
      <th>행정동명</th>
      <th>법정동명</th>
      <th>대지구분명</th>
      <th>지번주소</th>
      <th>도로명</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>90956</td>
      <td>90956</td>
      <td>90956</td>
      <td>91280</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
      <td>91335</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>56910</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>34</td>
      <td>34</td>
      <td>17</td>
      <td>228</td>
      <td>2791</td>
      <td>2822</td>
      <td>2</td>
      <td>53118</td>
      <td>16610</td>
      <td>54142</td>
      <td>54031</td>
    </tr>
    <tr>
      <th>top</th>
      <td>리원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>경기도</td>
      <td>서구</td>
      <td>중앙동</td>
      <td>중동</td>
      <td>대지</td>
      <td>서울특별시 동대문구 제기동 965-1</td>
      <td>서울특별시 강남구 강남대로</td>
      <td>1123010300109650001031604</td>
      <td>서울특별시 동대문구 약령중앙로8길 10</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>152</td>
      <td>91335</td>
      <td>91335</td>
      <td>60774</td>
      <td>60774</td>
      <td>18964</td>
      <td>18964</td>
      <td>21374</td>
      <td>3165</td>
      <td>1856</td>
      <td>874</td>
      <td>91213</td>
      <td>198</td>
      <td>326</td>
      <td>198</td>
      <td>198</td>
    </tr>
  </tbody>
</table>
</div>



# 중복 제거한 값 보기


```python
df['상권업종대분류명'].unique()
```




    array(['의료'], dtype=object)




```python
df['상권업종대분류명'].nunique() #엔유니크는 갯수를 세어준다.
```




    1




```python
df['상권업종중분류명']
```




    0              병원
    1              병원
    2              병원
    3              병원
    4          약국/한약방
               ...   
    91330      약국/한약방
    91331    의료관련서비스업
    91332          병원
    91333          병원
    91334          병원
    Name: 상권업종중분류명, Length: 91335, dtype: object




```python
df['상권업종중분류명'].unique()
```




    array(['병원', '약국/한약방', '수의업', '유사의료업', '의료관련서비스업'], dtype=object)




```python
df['상권업종중분류명'].nunique()
```




    5




```python
df['상권업종소분류명'].unique()
```




    array(['산부인과', '내과/외과', '신경외과', '기타병원', '약국', '동물병원', '한약방', '탕제원',
           '정형/성형외과', '소아과', '이비인후과의원', '노인/치매병원', '언어치료', '수의업-종합', '한의원',
           '치과의원', '침구원', '일반병원', '안과의원', '조산원', '한방병원', '종합병원', '유사의료업기타',
           '응급구조대', '혈액원', '치과병원', '척추교정치료', '피부과', '비뇨기과', '치과기공소', '산후조리원',
           '접골원', '수의업-기타', '제대혈'], dtype=object)




```python
df['상권업종소분류명'].nunique()
```




    34




```python
df['시도명']
```




    0          경기도
    1        서울특별시
    2          경기도
    3        부산광역시
    4          경기도
             ...  
    91330    대전광역시
    91331      경기도
    91332    부산광역시
    91333    서울특별시
    91334     충청남도
    Name: 시도명, Length: 91335, dtype: object




```python
city= df['시도명'].value_counts() #데이터수 세어보기
```


```python
city_normalize=df['시도명'].value_counts(normalize=True) #비율을 계산해준다.
```


```python
city_normalize.plot()
```




    <AxesSubplot:>




    
![png](output_46_1.png)
    



```python
city.plot.barh()
```




    <AxesSubplot:>




    
![png](output_47_1.png)
    



```python
city_normalize.plot.pie(figsize=(7,7))
```

    C:\Users\cityo\anaconda3\lib\site-packages\pandas\plotting\_matplotlib\core.py:1583: MatplotlibDeprecationWarning: normalize=None does not normalize if the sum is less than 1 but this behavior is deprecated since 3.3 until two minor releases later. After the deprecation period the default value will be normalize=True. To prevent normalization pass normalize=False 
      results = ax.pie(y, labels=blabels, **kwds)
    




    <AxesSubplot:ylabel='시도명'>




    
![png](output_48_2.png)
    



```python
#seaborn ,sns
c= sns.countplot(data=df, y='시도명' ) #변수명으로 담아주면 설명이 출력 안됌
```


    
![png](output_49_0.png)
    



```python
df['상권업종대분류명'].value_counts()
```




    의료    91335
    Name: 상권업종대분류명, dtype: int64




```python
n=df['상권업종중분류명'].value_counts(normalize=True)
```


```python
n.plot.bar(rot=0) #rot=0:글자세워주기
```




    <AxesSubplot:>




    
![png](output_52_1.png)
    



```python
n.plot.pie()
```




    <AxesSubplot:ylabel='상권업종중분류명'>




    
![png](output_53_1.png)
    



```python
df['상권업종소분류명'].value_counts(normalize=True)
```




    약국         0.207631
    치과의원       0.150337
    한의원        0.144643
    내과/외과      0.124531
    기타병원       0.053890
    일반병원       0.037061
    동물병원       0.033919
    정형/성형외과    0.028051
    소아과        0.027065
    수의업-종합     0.024262
    치과기공소      0.018876
    이비인후과의원    0.016270
    한약방        0.015788
    피부과        0.013938
    산부인과       0.012219
    노인/치매병원    0.011551
    안과의원       0.011409
    비뇨기과       0.008858
    종합병원       0.008343
    치과병원       0.008277
    언어치료       0.007270
    유사의료업기타    0.006887
    탕제원        0.005660
    산후조리원      0.005595
    신경외과       0.004609
    한방병원       0.004347
    척추교정치료     0.003701
    침구원        0.001686
    혈액원        0.001423
    응급구조대      0.001369
    조산원        0.000328
    접골원        0.000099
    수의업-기타     0.000099
    제대혈        0.000011
    Name: 상권업종소분류명, dtype: float64




```python
xy=df['상권업종소분류명'].value_counts()
```


```python
xy.plot.barh(figsize=(7,9),grid=True)
```




    <AxesSubplot:>




    
![png](output_56_1.png)
    


## 데이터 색인하기


```python
df_medical=df[df['상권업종중분류명'] == '약국/한약방'].copy()
df_medical
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>...</th>
      <th>지번주소</th>
      <th>도로명코드</th>
      <th>도로명</th>
      <th>건물본번지</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>20364049</td>
      <td>더블유스토어수지점</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>경기도</td>
      <td>41465.0</td>
      <td>...</td>
      <td>경기도 용인시 수지구 풍덕천동 712-2</td>
      <td>414653205024</td>
      <td>경기도 용인시 수지구 문정로</td>
      <td>32</td>
      <td>4146510100107120002026238</td>
      <td>경기도 용인시 수지구 문정로 32</td>
      <td>448170.0</td>
      <td>16837.0</td>
      <td>127.095522</td>
      <td>37.323528</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20733252</td>
      <td>춘산한약방</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A02</td>
      <td>한약방</td>
      <td>강원도</td>
      <td>42110.0</td>
      <td>...</td>
      <td>강원도 춘천시 중앙로2가 99</td>
      <td>421104454113</td>
      <td>강원도 춘천시 낙원길</td>
      <td>50</td>
      <td>4211010500101000000023668</td>
      <td>강원도 춘천시 낙원길 50</td>
      <td>200042.0</td>
      <td>24273.0</td>
      <td>127.726905</td>
      <td>37.880504</td>
    </tr>
    <tr>
      <th>7</th>
      <td>20582210</td>
      <td>부부탕제원</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A03</td>
      <td>탕제원</td>
      <td>충청북도</td>
      <td>43111.0</td>
      <td>...</td>
      <td>충청북도 청주시 상당구 금천동 187-17</td>
      <td>431114508623</td>
      <td>충청북도 청주시 상당구 중고개로337번길</td>
      <td>134</td>
      <td>4311112000101870017042942</td>
      <td>충청북도 청주시 상당구 중고개로337번길 134</td>
      <td>360802.0</td>
      <td>28726.0</td>
      <td>127.499206</td>
      <td>36.625355</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21057519</td>
      <td>민생약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>경상남도</td>
      <td>48890.0</td>
      <td>...</td>
      <td>경상남도 합천군 용주면 월평리 78-2</td>
      <td>488904844473</td>
      <td>경상남도 합천군 용주면 월평길</td>
      <td>149</td>
      <td>4889046030200780002048274</td>
      <td>경상남도 합천군 용주면 월평길 149-35</td>
      <td>678912.0</td>
      <td>50212.0</td>
      <td>128.118615</td>
      <td>35.575962</td>
    </tr>
    <tr>
      <th>13</th>
      <td>21217689</td>
      <td>제중당한약방</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A02</td>
      <td>한약방</td>
      <td>전라남도</td>
      <td>46830.0</td>
      <td>...</td>
      <td>전라남도 영암군 도포면 덕화리 296</td>
      <td>468304685396</td>
      <td>전라남도 영암군 도포면 인덕길</td>
      <td>75</td>
      <td>4683035023102960000000001</td>
      <td>전라남도 영암군 도포면 인덕길 75-10</td>
      <td>526832.0</td>
      <td>58429.0</td>
      <td>126.630348</td>
      <td>34.834080</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>91312</th>
      <td>16131397</td>
      <td>큰나무약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>경기도</td>
      <td>41281.0</td>
      <td>...</td>
      <td>경기도 고양시 덕양구 성사동 700-11</td>
      <td>412812192001</td>
      <td>경기도 고양시 덕양구 고양대로</td>
      <td>1361</td>
      <td>4128110600107000011013834</td>
      <td>경기도 고양시 덕양구 고양대로 1361</td>
      <td>412807.0</td>
      <td>10464.0</td>
      <td>126.835684</td>
      <td>37.655048</td>
    </tr>
    <tr>
      <th>91321</th>
      <td>16130841</td>
      <td>복음약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>대구광역시</td>
      <td>27290.0</td>
      <td>...</td>
      <td>대구광역시 달서구 본동 276</td>
      <td>272904241030</td>
      <td>대구광역시 달서구 구마로36길</td>
      <td>33</td>
      <td>2729012400102760000029818</td>
      <td>대구광역시 달서구 구마로36길 33</td>
      <td>704752.0</td>
      <td>42735.0</td>
      <td>128.547352</td>
      <td>35.836250</td>
    </tr>
    <tr>
      <th>91322</th>
      <td>16091491</td>
      <td>설연화한복감성약방</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>서울특별시</td>
      <td>11260.0</td>
      <td>...</td>
      <td>서울특별시 중랑구 묵동 174-1</td>
      <td>112603005050</td>
      <td>서울특별시 중랑구 공릉로</td>
      <td>28</td>
      <td>1126010400101740001009985</td>
      <td>서울특별시 중랑구 공릉로 28</td>
      <td>131848.0</td>
      <td>2034.0</td>
      <td>127.078082</td>
      <td>37.613194</td>
    </tr>
    <tr>
      <th>91324</th>
      <td>16109731</td>
      <td>위례수약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>경기도</td>
      <td>41131.0</td>
      <td>...</td>
      <td>경기도 성남시 수정구 창곡동 559-4</td>
      <td>411313350738</td>
      <td>경기도 성남시 수정구 위례서일로</td>
      <td>18</td>
      <td>4113110800101810002000002</td>
      <td>경기도 성남시 수정구 위례서일로 18</td>
      <td>461210.0</td>
      <td>13647.0</td>
      <td>127.137870</td>
      <td>37.465260</td>
    </tr>
    <tr>
      <th>91330</th>
      <td>16196725</td>
      <td>온누리약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>대전광역시</td>
      <td>30170.0</td>
      <td>...</td>
      <td>대전광역시 서구 둔산동 1507</td>
      <td>301703166026</td>
      <td>대전광역시 서구 문예로</td>
      <td>67</td>
      <td>3017011200115070000021096</td>
      <td>대전광역시 서구 문예로 67</td>
      <td>302831.0</td>
      <td>35240.0</td>
      <td>127.389865</td>
      <td>36.352728</td>
    </tr>
  </tbody>
</table>
<p>20923 rows × 29 columns</p>
</div>




```python
df_medical.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>...</th>
      <th>지번주소</th>
      <th>도로명코드</th>
      <th>도로명</th>
      <th>건물본번지</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>20364049</td>
      <td>더블유스토어수지점</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>경기도</td>
      <td>41465.0</td>
      <td>...</td>
      <td>경기도 용인시 수지구 풍덕천동 712-2</td>
      <td>414653205024</td>
      <td>경기도 용인시 수지구 문정로</td>
      <td>32</td>
      <td>4146510100107120002026238</td>
      <td>경기도 용인시 수지구 문정로 32</td>
      <td>448170.0</td>
      <td>16837.0</td>
      <td>127.095522</td>
      <td>37.323528</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 29 columns</p>
</div>




```python
m=df['상권업종대분류명'] == '의료'
df.loc[m,'상권업종중분류명'].value_counts()
```




    병원          60774
    약국/한약방      20923
    수의업          5323
    유사의료업        3774
    의료관련서비스업      541
    Name: 상권업종중분류명, dtype: int64




```python
df_medi=df[df['상권업종중분류명']== '유사의료업']#행렬수 보여준다.
df_medi.shape
```




    (3774, 29)




```python
df['상호명'].value_counts().head()
```




    리원       152
    온누리약국    149
    경희한의원    141
    우리약국     119
    중앙약국     111
    Name: 상호명, dtype: int64




```python
df['상호명'].value_counts().tail(10)
```




    한국아동발달지원센터    1
    박승호방사선과의원     1
    한우리이비인후과의원    1
    세아치과의원        1
    대화약업사         1
    미소미함치과의원      1
    노바치과          1
    연성한의원         1
    하나인치과병원       1
    광명유안과         1
    Name: 상호명, dtype: int64




```python
df_medi['상호명'].value_counts().head(10) #유사의료업만.
```




    리원           32
    고려수지침        22
    대한적십자사       17
    헌혈의집         12
    고려수지침학회      10
    수치과기공소       10
    제일치과기공소       9
    미소치과기공소       8
    아트치과기공소       8
    대한응급환자이송단     8
    Name: 상호명, dtype: int64



## 여러 조건으로 색인하기


```python
(df['상권업종소분류명']=='약국') & (df['시도명']=='서울특별시')
```




    0        False
    1        False
    2        False
    3        False
    4        False
             ...  
    91330    False
    91331    False
    91332    False
    91333    False
    91334    False
    Length: 91335, dtype: bool




```python
df_seoul_drug=df[(df['상권업종소분류명']=='약국') & (df['시도명']=='서울특별시')]
print(df_seoul_drug.shape) #print 구문을 사용하면 아래와 함께 두개의 데이터 출력가능
df_seoul_drug.head()
```

    (3579, 29)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>...</th>
      <th>지번주소</th>
      <th>도로명코드</th>
      <th>도로명</th>
      <th>건물본번지</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33</th>
      <td>20816709</td>
      <td>이즈타워약</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>서울특별시</td>
      <td>11680.0</td>
      <td>...</td>
      <td>서울특별시 강남구 역삼동 821</td>
      <td>116803122010</td>
      <td>서울특별시 강남구 테헤란로</td>
      <td>101</td>
      <td>1168010100108210001000001</td>
      <td>서울특별시 강남구 테헤란로 101</td>
      <td>135080.0</td>
      <td>6134.0</td>
      <td>127.028023</td>
      <td>37.498656</td>
    </tr>
    <tr>
      <th>51</th>
      <td>20855710</td>
      <td>진흥약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>서울특별시</td>
      <td>11740.0</td>
      <td>...</td>
      <td>서울특별시 강동구 둔촌동 630</td>
      <td>117403124002</td>
      <td>서울특별시 강동구 명일로</td>
      <td>172</td>
      <td>1174010600106090000000001</td>
      <td>서울특별시 강동구 명일로 172</td>
      <td>134767.0</td>
      <td>5360.0</td>
      <td>127.145055</td>
      <td>37.534135</td>
    </tr>
    <tr>
      <th>130</th>
      <td>21589838</td>
      <td>신세계약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>서울특별시</td>
      <td>11260.0</td>
      <td>...</td>
      <td>서울특별시 중랑구 신내동 646</td>
      <td>112603106007</td>
      <td>서울특별시 중랑구 신내로</td>
      <td>211</td>
      <td>1126010600106460000000300</td>
      <td>서울특별시 중랑구 신내로 211</td>
      <td>131130.0</td>
      <td>2024.0</td>
      <td>127.092597</td>
      <td>37.616424</td>
    </tr>
    <tr>
      <th>136</th>
      <td>22388303</td>
      <td>메디팜한솔약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>서울특별시</td>
      <td>11200.0</td>
      <td>...</td>
      <td>서울특별시 성동구 행당동 346</td>
      <td>112003103006</td>
      <td>서울특별시 성동구 행당로</td>
      <td>82</td>
      <td>1120010700103460012016935</td>
      <td>서울특별시 성동구 행당로 82</td>
      <td>133777.0</td>
      <td>4717.0</td>
      <td>127.027513</td>
      <td>37.556238</td>
    </tr>
    <tr>
      <th>141</th>
      <td>22412563</td>
      <td>명약국</td>
      <td>S</td>
      <td>의료</td>
      <td>S02</td>
      <td>약국/한약방</td>
      <td>S02A01</td>
      <td>약국</td>
      <td>서울특별시</td>
      <td>11230.0</td>
      <td>...</td>
      <td>서울특별시 동대문구 휘경동 286-121</td>
      <td>112304115120</td>
      <td>서울특별시 동대문구 망우로18나길</td>
      <td>3</td>
      <td>1123010900102860121007257</td>
      <td>서울특별시 동대문구 망우로18나길 3</td>
      <td>130090.0</td>
      <td>2498.0</td>
      <td>127.060556</td>
      <td>37.587349</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 29 columns</p>
</div>




```python
c=df_seoul_drug['시군구명'].value_counts()
c.head()
```




    강남구     374
    동대문구    261
    광진구     212
    서초구     191
    송파구     188
    Name: 시군구명, dtype: int64




```python
df_seoul_drug['시군구명'].value_counts(normalize=True)
```




    강남구     0.104498
    동대문구    0.072925
    광진구     0.059234
    서초구     0.053367
    송파구     0.052529
    노원구     0.047220
    성북구     0.044705
    은평구     0.042191
    영등포구    0.040514
    강서구     0.037999
    마포구     0.037999
    중랑구     0.036044
    서대문구    0.033529
    관악구     0.032970
    강동구     0.032691
    종로구     0.031014
    양천구     0.030455
    중구      0.029617
    강북구     0.029058
    구로구     0.028500
    동작구     0.026823
    성동구     0.024588
    용산구     0.024308
    금천구     0.023750
    도봉구     0.023470
    Name: 시군구명, dtype: float64




```python
c.plot.bar(rot=60)
```




    <AxesSubplot:>




    
![png](output_70_1.png)
    



```python
df_seoul_hospital=df[(df['상권업종소분류명'] == '종합병원' ) &
                     (df['시도명']=='서울특별시')].copy()
df_seoul_hospital
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>...</th>
      <th>지번주소</th>
      <th>도로명코드</th>
      <th>도로명</th>
      <th>건물본번지</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>305</th>
      <td>25155642</td>
      <td>대진의료재단</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11215.0</td>
      <td>...</td>
      <td>서울특별시 광진구 중곡동 58-25</td>
      <td>112153104006</td>
      <td>서울특별시 광진구 긴고랑로</td>
      <td>119</td>
      <td>1121510100100580025000733</td>
      <td>서울특별시 광진구 긴고랑로 119</td>
      <td>143220.0</td>
      <td>4944.0</td>
      <td>127.088279</td>
      <td>37.559048</td>
    </tr>
    <tr>
      <th>353</th>
      <td>20471487</td>
      <td>홍익병원별관</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11470.0</td>
      <td>...</td>
      <td>서울특별시 양천구 신정동 897-13</td>
      <td>114702005008</td>
      <td>서울특별시 양천구 국회대로</td>
      <td>250</td>
      <td>1147010100108970013001044</td>
      <td>서울특별시 양천구 국회대로 250</td>
      <td>158070.0</td>
      <td>7937.0</td>
      <td>126.862805</td>
      <td>37.529213</td>
    </tr>
    <tr>
      <th>385</th>
      <td>20737057</td>
      <td>SNUH</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11680.0</td>
      <td>...</td>
      <td>서울특별시 강남구 역삼동 736-55</td>
      <td>116804166727</td>
      <td>서울특별시 강남구 테헤란로26길</td>
      <td>10</td>
      <td>1168010100107360055027688</td>
      <td>서울특별시 강남구 테헤란로26길 10</td>
      <td>135080.0</td>
      <td>6236.0</td>
      <td>127.035825</td>
      <td>37.499630</td>
    </tr>
    <tr>
      <th>1917</th>
      <td>23210677</td>
      <td>평화드림여의도성모병원의료기매장</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11560.0</td>
      <td>...</td>
      <td>서울특별시 영등포구 여의도동 62</td>
      <td>115603118001</td>
      <td>서울특별시 영등포구 63로</td>
      <td>10</td>
      <td>1156011000100620000031477</td>
      <td>서울특별시 영등포구 63로 10</td>
      <td>150713.0</td>
      <td>7345.0</td>
      <td>126.936693</td>
      <td>37.518296</td>
    </tr>
    <tr>
      <th>2461</th>
      <td>20024045</td>
      <td>한양</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11200.0</td>
      <td>...</td>
      <td>서울특별시 성동구 행당동 15-1</td>
      <td>112003103002</td>
      <td>서울특별시 성동구 마조로</td>
      <td>22</td>
      <td>1120010700100150001019623</td>
      <td>서울특별시 성동구 마조로 22-2</td>
      <td>133070.0</td>
      <td>4763.0</td>
      <td>127.041325</td>
      <td>37.559469</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>71991</th>
      <td>28505952</td>
      <td>서울성모병원응급의료센터</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11650.0</td>
      <td>...</td>
      <td>서울특별시 서초구 반포동 505</td>
      <td>116502121003</td>
      <td>서울특별시 서초구 반포대로</td>
      <td>222</td>
      <td>1165010700101230000017226</td>
      <td>서울특별시 서초구 반포대로 222</td>
      <td>137701.0</td>
      <td>6591.0</td>
      <td>127.005841</td>
      <td>37.502382</td>
    </tr>
    <tr>
      <th>76508</th>
      <td>12292992</td>
      <td>라마르의원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11740.0</td>
      <td>...</td>
      <td>서울특별시 강동구 천호동 453-8</td>
      <td>117404172367</td>
      <td>서울특별시 강동구 천호대로157길</td>
      <td>18</td>
      <td>1174010900104530021010314</td>
      <td>서울특별시 강동구 천호대로157길 18</td>
      <td>134864.0</td>
      <td>5335.0</td>
      <td>127.127466</td>
      <td>37.538485</td>
    </tr>
    <tr>
      <th>90492</th>
      <td>16031909</td>
      <td>가톨릭대학교여의도성모병원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11140.0</td>
      <td>...</td>
      <td>서울특별시 중구 명동2가 1-1</td>
      <td>111404103165</td>
      <td>서울특별시 중구 명동길</td>
      <td>74</td>
      <td>1114012700100010001019574</td>
      <td>서울특별시 중구 명동길 74</td>
      <td>100809.0</td>
      <td>4537.0</td>
      <td>126.986758</td>
      <td>37.563662</td>
    </tr>
    <tr>
      <th>90581</th>
      <td>16332576</td>
      <td>씨엠병원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11560.0</td>
      <td>...</td>
      <td>서울특별시 영등포구 영등포동4가 90</td>
      <td>115604154717</td>
      <td>서울특별시 영등포구 영등포로36길</td>
      <td>13</td>
      <td>1156010500100900000035097</td>
      <td>서울특별시 영등포구 영등포로36길 13</td>
      <td>150030.0</td>
      <td>7301.0</td>
      <td>126.903857</td>
      <td>37.518807</td>
    </tr>
    <tr>
      <th>90788</th>
      <td>16162338</td>
      <td>성베드로병원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11680.0</td>
      <td>...</td>
      <td>서울특별시 강남구 도곡동 910-27</td>
      <td>116802000003</td>
      <td>서울특별시 강남구 남부순환로</td>
      <td>2649</td>
      <td>1168011800109100027000895</td>
      <td>서울특별시 강남구 남부순환로 2649</td>
      <td>135859.0</td>
      <td>6271.0</td>
      <td>127.039567</td>
      <td>37.485604</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 29 columns</p>
</div>




```python
df_seoul_hospital['시군구명'].value_counts()
```




    강남구     15
    영등포구     8
    광진구      6
    서초구      6
    중구       5
    강동구      5
    송파구      5
    서대문구     4
    도봉구      4
    강북구      4
    양천구      4
    성북구      3
    노원구      2
    동대문구     2
    종로구      2
    구로구      2
    강서구      2
    관악구      2
    성동구      2
    중랑구      2
    금천구      2
    용산구      1
    은평구      1
    마포구      1
    동작구      1
    Name: 시군구명, dtype: int64



## 텍스트 데이터 색인하기


```python
#색인하기 전에 상호명 중에 종합병원이 아닌 데이터를 찾아본다.
df_seoul_hospital['상호명'].str.contains('종합병원')
```




    305      False
    353      False
    385      False
    1917     False
    2461     False
             ...  
    71991    False
    76508    False
    90492    False
    90581    False
    90788    False
    Name: 상호명, Length: 91, dtype: bool




```python
~df_seoul_hospital['상호명'].str.contains('종합병원') # ~ 표시는 반대의경우를 가져온다.
```




    305      True
    353      True
    385      True
    1917     True
    2461     True
             ... 
    71991    True
    76508    True
    90492    True
    90581    True
    90788    True
    Name: 상호명, Length: 91, dtype: bool




```python
df_seoul_hospital[~df_seoul_hospital['상호명'].str.contains('종합병원')] # ~ 표시는 반대의경우를 가져온다.
#종합병원이라는 텍스트가 안들어간 데이터경우
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>...</th>
      <th>지번주소</th>
      <th>도로명코드</th>
      <th>도로명</th>
      <th>건물본번지</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>305</th>
      <td>25155642</td>
      <td>대진의료재단</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11215.0</td>
      <td>...</td>
      <td>서울특별시 광진구 중곡동 58-25</td>
      <td>112153104006</td>
      <td>서울특별시 광진구 긴고랑로</td>
      <td>119</td>
      <td>1121510100100580025000733</td>
      <td>서울특별시 광진구 긴고랑로 119</td>
      <td>143220.0</td>
      <td>4944.0</td>
      <td>127.088279</td>
      <td>37.559048</td>
    </tr>
    <tr>
      <th>353</th>
      <td>20471487</td>
      <td>홍익병원별관</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11470.0</td>
      <td>...</td>
      <td>서울특별시 양천구 신정동 897-13</td>
      <td>114702005008</td>
      <td>서울특별시 양천구 국회대로</td>
      <td>250</td>
      <td>1147010100108970013001044</td>
      <td>서울특별시 양천구 국회대로 250</td>
      <td>158070.0</td>
      <td>7937.0</td>
      <td>126.862805</td>
      <td>37.529213</td>
    </tr>
    <tr>
      <th>385</th>
      <td>20737057</td>
      <td>SNUH</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11680.0</td>
      <td>...</td>
      <td>서울특별시 강남구 역삼동 736-55</td>
      <td>116804166727</td>
      <td>서울특별시 강남구 테헤란로26길</td>
      <td>10</td>
      <td>1168010100107360055027688</td>
      <td>서울특별시 강남구 테헤란로26길 10</td>
      <td>135080.0</td>
      <td>6236.0</td>
      <td>127.035825</td>
      <td>37.499630</td>
    </tr>
    <tr>
      <th>1917</th>
      <td>23210677</td>
      <td>평화드림여의도성모병원의료기매장</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11560.0</td>
      <td>...</td>
      <td>서울특별시 영등포구 여의도동 62</td>
      <td>115603118001</td>
      <td>서울특별시 영등포구 63로</td>
      <td>10</td>
      <td>1156011000100620000031477</td>
      <td>서울특별시 영등포구 63로 10</td>
      <td>150713.0</td>
      <td>7345.0</td>
      <td>126.936693</td>
      <td>37.518296</td>
    </tr>
    <tr>
      <th>2461</th>
      <td>20024045</td>
      <td>한양</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11200.0</td>
      <td>...</td>
      <td>서울특별시 성동구 행당동 15-1</td>
      <td>112003103002</td>
      <td>서울특별시 성동구 마조로</td>
      <td>22</td>
      <td>1120010700100150001019623</td>
      <td>서울특별시 성동구 마조로 22-2</td>
      <td>133070.0</td>
      <td>4763.0</td>
      <td>127.041325</td>
      <td>37.559469</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>71991</th>
      <td>28505952</td>
      <td>서울성모병원응급의료센터</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11650.0</td>
      <td>...</td>
      <td>서울특별시 서초구 반포동 505</td>
      <td>116502121003</td>
      <td>서울특별시 서초구 반포대로</td>
      <td>222</td>
      <td>1165010700101230000017226</td>
      <td>서울특별시 서초구 반포대로 222</td>
      <td>137701.0</td>
      <td>6591.0</td>
      <td>127.005841</td>
      <td>37.502382</td>
    </tr>
    <tr>
      <th>76508</th>
      <td>12292992</td>
      <td>라마르의원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11740.0</td>
      <td>...</td>
      <td>서울특별시 강동구 천호동 453-8</td>
      <td>117404172367</td>
      <td>서울특별시 강동구 천호대로157길</td>
      <td>18</td>
      <td>1174010900104530021010314</td>
      <td>서울특별시 강동구 천호대로157길 18</td>
      <td>134864.0</td>
      <td>5335.0</td>
      <td>127.127466</td>
      <td>37.538485</td>
    </tr>
    <tr>
      <th>90492</th>
      <td>16031909</td>
      <td>가톨릭대학교여의도성모병원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11140.0</td>
      <td>...</td>
      <td>서울특별시 중구 명동2가 1-1</td>
      <td>111404103165</td>
      <td>서울특별시 중구 명동길</td>
      <td>74</td>
      <td>1114012700100010001019574</td>
      <td>서울특별시 중구 명동길 74</td>
      <td>100809.0</td>
      <td>4537.0</td>
      <td>126.986758</td>
      <td>37.563662</td>
    </tr>
    <tr>
      <th>90581</th>
      <td>16332576</td>
      <td>씨엠병원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11560.0</td>
      <td>...</td>
      <td>서울특별시 영등포구 영등포동4가 90</td>
      <td>115604154717</td>
      <td>서울특별시 영등포구 영등포로36길</td>
      <td>13</td>
      <td>1156010500100900000035097</td>
      <td>서울특별시 영등포구 영등포로36길 13</td>
      <td>150030.0</td>
      <td>7301.0</td>
      <td>126.903857</td>
      <td>37.518807</td>
    </tr>
    <tr>
      <th>90788</th>
      <td>16162338</td>
      <td>성베드로병원</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11680.0</td>
      <td>...</td>
      <td>서울특별시 강남구 도곡동 910-27</td>
      <td>116802000003</td>
      <td>서울특별시 강남구 남부순환로</td>
      <td>2649</td>
      <td>1168011800109100027000895</td>
      <td>서울특별시 강남구 남부순환로 2649</td>
      <td>135859.0</td>
      <td>6271.0</td>
      <td>127.039567</td>
      <td>37.485604</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 29 columns</p>
</div>




```python
df_seoul_hospital.loc[~df_seoul_hospital['상호명'].str.contains('종합병원'),'상호명'].unique() # ~ 표시는 반대의경우를 가져온다.

```




    array(['대진의료재단', '홍익병원별관', 'SNUH', '평화드림여의도성모병원의료기매장', '한양', '백산의료재단친구병원',
           '서울보훈병원', '서울성모병원장례식장꽃배달', '서울대학교병원', '알콜중독및정신질환상담소',
           '강남성모병원장례식장꽃배달', '제일병원', '이랜드클리닉', '사랑나눔의료재단', '우울증센터', '성심의료재단',
           '다나의료재단', '서울아산병원신관', '원자력병원장례식장', '국민의원', '고려대학교구로병원', '학교법인일송학원',
           '삼성의료원장례식장', '희명스포츠의학센터인공신장실', '연세대학교의과대학강남세브란스', '국립정신병원',
           '코아클리닉', '수서제일의원', '사랑의의원', '한국전력공사부속한일병원', '신촌연세병원', '창동제일의원',
           '영동세브란스병원', '제일성심의원', '삼성의료재단강북삼성태', '서울시립보라매병원', '서울이의원',
           '서울대학교병원비상계획외래', '평화드림서울성모병원의료', '홍익병원', '사랑나눔의료재단서', '독일의원',
           '서울연합의원', '우신향병원', '동부제일병원', '아산재단금강병원', '명곡안연구소', '아산재단서울중앙병원',
           '메디힐특수여객', '삼성생명공익재단삼성서', '성광의료재단차병원', '한국건강관리협회서울특',
           '정해복지부설한신메디피아', '성베드로병원', '성애의료재단', '실로암의원', 'Y&T성모마취과', '광진성모의원',
           '서울현대의원', '이노신경과의원', '송정훼밀리의원', '서울중앙의원', '영남의료재단', '인제대학교서울백병원',
           '한국필의료재단', '세브란스의원', '가톨릭대학교성바오로병원장례식장', '서울연세의원', '사랑의병원',
           '성삼의료재단미즈메디병원', '씨엠충무병원', '성신의원', '원진재단부설녹색병원', '송파제일의원',
           '카톨릭성모의원', '한양성심의원', '관악성모의원', '강남센트럴병원', '우이한솔의원', '우리들병원',
           '서울성모병원어린이집', '건국대학교병원', '서울적십자병원', '북부성모의원', '한림대학교부속한강성심병원장례식장',
           '서울성모병원응급의료센터', '라마르의원', '가톨릭대학교여의도성모병원', '씨엠병원'], dtype=object)



## 필요없는 데이터 삭제하기


```python
df_seoul_hospital[df_seoul_hospital['상호명'].str.contains('꽃배달')]
# 텍스트 '꽃배달'을 포함하는 경우
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>...</th>
      <th>지번주소</th>
      <th>도로명코드</th>
      <th>도로명</th>
      <th>건물본번지</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2803</th>
      <td>20895655</td>
      <td>서울성모병원장례식장꽃배달</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11650.0</td>
      <td>...</td>
      <td>서울특별시 서초구 반포동 551</td>
      <td>116504163330</td>
      <td>서울특별시 서초구 사평대로28길</td>
      <td>55</td>
      <td>1165010700105510000017194</td>
      <td>서울특별시 서초구 사평대로28길 55</td>
      <td>137040.0</td>
      <td>6578.0</td>
      <td>127.000682</td>
      <td>37.498257</td>
    </tr>
    <tr>
      <th>4644</th>
      <td>22020310</td>
      <td>강남성모병원장례식장꽃배달</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11650.0</td>
      <td>...</td>
      <td>서울특별시 서초구 반포동 547-6</td>
      <td>116504163242</td>
      <td>서울특별시 서초구 반포대로39길</td>
      <td>56</td>
      <td>1165010700105470006016762</td>
      <td>서울특별시 서초구 반포대로39길 56-24</td>
      <td>137040.0</td>
      <td>6578.0</td>
      <td>127.001756</td>
      <td>37.499095</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 29 columns</p>
</div>




```python
df_seoul_hospital[df_seoul_hospital['상호명'].str.contains('의료기')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상가업소번호</th>
      <th>상호명</th>
      <th>상권업종대분류코드</th>
      <th>상권업종대분류명</th>
      <th>상권업종중분류코드</th>
      <th>상권업종중분류명</th>
      <th>상권업종소분류코드</th>
      <th>상권업종소분류명</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>...</th>
      <th>지번주소</th>
      <th>도로명코드</th>
      <th>도로명</th>
      <th>건물본번지</th>
      <th>건물관리번호</th>
      <th>도로명주소</th>
      <th>구우편번호</th>
      <th>신우편번호</th>
      <th>경도</th>
      <th>위도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1917</th>
      <td>23210677</td>
      <td>평화드림여의도성모병원의료기매장</td>
      <td>S</td>
      <td>의료</td>
      <td>S01</td>
      <td>병원</td>
      <td>S01B01</td>
      <td>종합병원</td>
      <td>서울특별시</td>
      <td>11560.0</td>
      <td>...</td>
      <td>서울특별시 영등포구 여의도동 62</td>
      <td>115603118001</td>
      <td>서울특별시 영등포구 63로</td>
      <td>10</td>
      <td>1156011000100620000031477</td>
      <td>서울특별시 영등포구 63로 10</td>
      <td>150713.0</td>
      <td>7345.0</td>
      <td>126.936693</td>
      <td>37.518296</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 29 columns</p>
</div>




```python
drop_row=df_seoul_hospital[df_seoul_hospital['상호명'].str.contains('꽃배달|의료기|장례식장|상담소|어린이집')].index
drop_row = drop_row.tolist()
drop_row
```




    [1917, 2803, 4431, 4644, 7938, 10283, 47008, 60645, 70177]




```python
drop_row2=df_seoul_hospital[df_seoul_hospital['상호명'].str.endswith('의원')].index
drop_row2=drop_row2.tolist()         #endwith = 특정단어를 찾아낼 수 있다.
drop_row2
```




    [8479,
     12854,
     13715,
     14966,
     16091,
     18047,
     20200,
     20415,
     30706,
     32889,
     34459,
     34720,
     35696,
     37251,
     45120,
     49626,
     51575,
     55133,
     56320,
     56404,
     56688,
     57551,
     62113,
     76508]




```python
drop_row=drop_row+drop_row2
len(drop_row)
```




    57




```python
print(df_seoul_hospital.shape)
df_seoul_hospital=df_seoul_hospital.drop(drop_row,axis=0) #인덱스는 행이라 0으로 삭제
print(df_seoul_hospital.shape)
```

    (91, 29)
    (58, 29)
    


```python
df_seoul_hospital['시군구명'].value_counts().plot.bar()
```




    <AxesSubplot:>




    
![png](output_85_1.png)
    



```python
plt.figure(figsize=(15,4))
sns.countplot(data=df_seoul_hospital, x='시군구명',order=df_seoul_hospital['시군구명'].value_counts().index)
# order = 큰 순위부터 그래프에 배치
```




    <AxesSubplot:xlabel='시군구명', ylabel='count'>




    
![png](output_86_1.png)
    



```python
df_seoul_hospital['상호명'].unique()
```




    array(['대진의료재단', '홍익병원별관', 'SNUH', '한양', '백산의료재단친구병원', '서울보훈병원',
           '서울대학교병원', '제일병원', '이랜드클리닉', '사랑나눔의료재단', '우울증센터', '성심의료재단',
           '다나의료재단', '서울아산병원신관', '고려대학교구로병원', '학교법인일송학원', '희명스포츠의학센터인공신장실',
           '연세대학교의과대학강남세브란스', '국립정신병원', '코아클리닉', '한국전력공사부속한일병원', '신촌연세병원',
           '영동세브란스병원', '삼성의료재단강북삼성태', '서울시립보라매병원', '서울대학교병원비상계획외래',
           '평화드림서울성모병원의료', '홍익병원', '사랑나눔의료재단서', '우신향병원', '동부제일병원', '아산재단금강병원',
           '명곡안연구소', '아산재단서울중앙병원', '메디힐특수여객', '삼성생명공익재단삼성서', '성광의료재단차병원',
           '한국건강관리협회서울특', '정해복지부설한신메디피아', '성베드로병원', '성애의료재단', 'Y&T성모마취과',
           '영남의료재단', '인제대학교서울백병원', '한국필의료재단', '사랑의병원', '성삼의료재단미즈메디병원',
           '씨엠충무병원', '원진재단부설녹색병원', '강남센트럴병원', '우리들병원', '건국대학교병원', '서울적십자병원',
           '서울성모병원응급의료센터', '가톨릭대학교여의도성모병원', '씨엠병원'], dtype=object)



## 특정 지역만 보기


```python
df_seoul=df[df['시도명'] == '서울특별시'].copy()
df_seoul.shape
```




    (18943, 29)




```python
df_seoul['시군구명'].value_counts().plot.bar(figsize=(10,4),rot=30)
```




    <AxesSubplot:>




    
![png](output_90_1.png)
    



```python
plt.figure(figsize=(15,4))
sns.countplot(data=df_seoul, x='시군구명')
```




    <AxesSubplot:xlabel='시군구명', ylabel='count'>




    
![png](output_91_1.png)
    



```python
# pandas의 plot.scatter를 통해 경도와 위도를 표시
df_seoul[['경도','위도','시군구명']].plot.scatter(x='경도',y='위도',figsize=(8,7),grid=True)
```




    <AxesSubplot:xlabel='경도', ylabel='위도'>




    
![png](output_92_1.png)
    



```python
plt.figure(figsize=(9,8))
sns.scatterplot(data=df_seoul, x="경도",y='위도',hue='시군구명')# hue는 색상을 의미
```




    <AxesSubplot:xlabel='경도', ylabel='위도'>




    
![png](output_93_1.png)
    



```python
plt.figure(figsize=(9,8))
sns.scatterplot(data=df_seoul, x="경도",y='위도',hue='상권업종중분류명')
```




    <AxesSubplot:xlabel='경도', ylabel='위도'>




    
![png](output_94_1.png)
    



```python
plt.figure(figsize=(16,12))
sns.scatterplot(data=df[:], x="경도",y='위도',hue='시도명')
```




    <AxesSubplot:xlabel='경도', ylabel='위도'>




    
![png](output_95_1.png)
    

