# pandas : 
### numpy 기반으로 만들어 진 좀 더 복잡한 데이터 분석에 특화된 라이브러리


```python

```


```python
import pandas as pd
```


```python
s1 =pd.Series([10,20,30,40,50])  #d 데이터 앞에 인덱스도 같이 표시
s1
```




    0    10
    1    20
    2    30
    3    40
    4    50
    dtype: int64




```python
s1.index
print(s1.index)
```

    RangeIndex(start=0, stop=5, step=1)
    


```python
s1.values
```




    array([10, 20, 30, 40, 50], dtype=int64)




```python

```


```python
# 원소의 데이터가 달라도 된다.
```


```python
s2 = pd.Series(['a','b',2])
```


```python
s2
```




    0    a
    1    b
    2    2
    dtype: object




```python
s5 = pd.Series({'국어':100,'영어':95,'수학':90})   #키와 발류값을 입력하면 index 값 대신 키값이 들어간다.
```


```python
s5
```




    국어    100
    영어     95
    수학     90
    dtype: int64




```python

```

## 날짜자동생성


```python
import pandas as pd
```


```python
pd.date_range(start='2019-01-01',end='2019-01-08')   # start는 시작날짜, end는 끝 날짜. 하루씩 증가
```




    DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
                   '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08'],
                  dtype='datetime64[ns]', freq='D')




```python
pd.date_range(start='2021-06-08',periods=10) #10일간 하루씩 증가
```




    DatetimeIndex(['2021-06-08', '2021-06-09', '2021-06-10', '2021-06-11',
                   '2021-06-12', '2021-06-13', '2021-06-14', '2021-06-15',
                   '2021-06-16', '2021-06-17'],
                  dtype='datetime64[ns]', freq='D')




```python
pd.date_range(start='2019-01-01',periods=4,freq='2D')  #2일간 4번증가, freq= 증가주기
```




    DatetimeIndex(['2019-01-01', '2019-01-03', '2019-01-05', '2019-01-07'], dtype='datetime64[ns]', freq='2D')




```python
pd.date_range(start='2019-01-01',periods=4,freq='w')  #일주일씩 증가, freq= 증가주기
```




    DatetimeIndex(['2019-01-06', '2019-01-13', '2019-01-20', '2019-01-27'], dtype='datetime64[ns]', freq='W-SUN')



freq='QS' 분기  
freq='AS' 연도 첫날  
freq= 'H' 한시간 주기 


```python

```

# DataFrame을 활용한 데이터 생성


```python
pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]]) # 자동으로 인덱스와 컬럼이 생성
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
import pandas as pd

data =np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index_date=pd.date_range('2019-09-01',periods=4)
columns_list=['A','B','C']
pd.DataFrame(data,index=index_date,columns=columns_list)
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-09-01</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2019-09-02</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2019-09-03</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2019-09-04</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
table_data={'연도':[2015,2016,2016,2017,2017],
'지사':['한국','한국','미국','한국','미국'],
            '고객 수': [200,250,450,300,500]}

table_data
```




    {'연도': [2015, 2016, 2016, 2017, 2017],
     '지사': ['한국', '한국', '미국', '한국', '미국'],
     '고객 수': [200, 250, 450, 300, 500]}




```python
pd.DataFrame(table_data)
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
      <th>연도</th>
      <th>지사</th>
      <th>고객 수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>한국</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>한국</td>
      <td>250</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>미국</td>
      <td>450</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017</td>
      <td>한국</td>
      <td>300</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017</td>
      <td>미국</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame(table_data,columns=['연도','지사','고객 수'])   # columns 원하는 순서로 정렬
df
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
      <th>연도</th>
      <th>지사</th>
      <th>고객 수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>한국</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>한국</td>
      <td>250</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>미국</td>
      <td>450</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017</td>
      <td>한국</td>
      <td>300</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017</td>
      <td>미국</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index, df.columns, df.values
```




    (RangeIndex(start=0, stop=5, step=1),
     Index(['연도', '지사', '고객 수'], dtype='object'),
     array([[2015, '한국', 200],
            [2016, '한국', 250],
            [2016, '미국', 450],
            [2017, '한국', 300],
            [2017, '미국', 500]], dtype=object))




```python

```
