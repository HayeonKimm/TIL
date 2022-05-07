# Pandas DataFrame


```python
import numpy as np
```


```python
x= np.array([('Rex',9,0.525),('Fibo',3,1320)],dtype=[('name','U10'),('age','i4'),('weight','f4')])
```


```python
x
```




    array([('Rex', 9, 5.25e-01), ('Fibo', 3, 1.32e+03)],
          dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])




```python

```


```python
m={'a':40,'b':50}
```


```python
m
```




    {'a': 40, 'b': 50}




```python
m['a']
```




    40




```python
x['name']
```




    array(['Rex', 'Fibo'], dtype='<U10')




```python
x['age']
```




    array([9, 3])




```python
x['weight']
```




    array([5.25e-01, 1.32e+03], dtype=float32)




```python

```


```python
import numpy as np
import pandas as pd
```


```python
import sys
sys.version
```




    '3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]'




```python
np.__version__
```




    '1.20.3'




```python
pd.__version__
```




    '1.1.3'




```python
import pandas as pd
```


```python
table_data= {'봄':[256.5,266,241,244,312],
            '여름':[214,241,241,222,214],
            '가을':[124,123,422,123,212],
            '겨울':[213,124,21,231,222]}

columns_list=['봄','여름','가을','겨울']
index_list=['2012','2013','2014','2015','2016']

a=pd.DataFrame(table_data,columns=columns_list,index=index_list)
```


```python
a
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
      <th>봄</th>
      <th>여름</th>
      <th>가을</th>
      <th>겨울</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>256.5</td>
      <td>214</td>
      <td>124</td>
      <td>213</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>266.0</td>
      <td>241</td>
      <td>123</td>
      <td>124</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>241.0</td>
      <td>241</td>
      <td>422</td>
      <td>21</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>244.0</td>
      <td>222</td>
      <td>123</td>
      <td>231</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>312.0</td>
      <td>214</td>
      <td>212</td>
      <td>222</td>
    </tr>
  </tbody>
</table>
</div>




```python
a.mean(axis=1)
```




    2012    201.875
    2013    188.500
    2014    231.250
    2015    205.000
    2016    240.000
    dtype: float64




```python
df1=pd.DataFrame({'class':[50,20,20,10],
                 'class2':[30,20,10,20]})

df1
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
      <th>class</th>
      <th>class2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2=pd.DataFrame({'class':[20,20,30],
                 'class2':[30,20,10]})

df2
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
      <th>class</th>
      <th>class2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
a=df1.append(df2,ignore_index=True)
```

# 컬럼수가 맞지 않는 데이터 병합


```python
df3 =pd.DataFrame({'class':[20,30]})
df3
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
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>




```python
a.append(df3,ignore_index=True)
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
      <th>class</th>
      <th>class2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>30</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>20</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>30</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## 특정 열을 기준으로 통합하기

DataFrame_left_data.merge(DataFrame_right_data)


```python
df_A_B=pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                    '제품A':[100,150,200,130],
                    '제품B':[90,110,140,170]})
df_A_B
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
      <th>판매월</th>
      <th>제품A</th>
      <th>제품B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1월</td>
      <td>100</td>
      <td>90</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2월</td>
      <td>150</td>
      <td>110</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3월</td>
      <td>200</td>
      <td>140</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4월</td>
      <td>130</td>
      <td>170</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_C_D=pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                    '제품C':[112,141,203,134],
                    '제품D':[90,110,140,170]})
df_C_D
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
      <th>판매월</th>
      <th>제품C</th>
      <th>제품D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1월</td>
      <td>112</td>
      <td>90</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2월</td>
      <td>141</td>
      <td>110</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3월</td>
      <td>203</td>
      <td>140</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4월</td>
      <td>134</td>
      <td>170</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_A_B.merge(df_C_D)
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
      <th>판매월</th>
      <th>제품A</th>
      <th>제품B</th>
      <th>제품C</th>
      <th>제품D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1월</td>
      <td>100</td>
      <td>90</td>
      <td>112</td>
      <td>90</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2월</td>
      <td>150</td>
      <td>110</td>
      <td>141</td>
      <td>110</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3월</td>
      <td>200</td>
      <td>140</td>
      <td>203</td>
      <td>140</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4월</td>
      <td>130</td>
      <td>170</td>
      <td>134</td>
      <td>170</td>
    </tr>
  </tbody>
</table>
</div>



## 특정 열을 기준으로 공통데이터를 가진 두 데이터를 통합


```python
df_left=pd.DataFrame({'key':['A','B','C'],
                     'left':[1,2,3]})

df_left
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
      <th>key</th>
      <th>left</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_right=pd.DataFrame({'key':['A','B','D'],
                     'right':[4,5,6]})

df_right
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
      <th>key</th>
      <th>right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>D</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_left.merge(df_right)
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
      <th>key</th>
      <th>left</th>
      <th>right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_left.merge(df_right,how='left')
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
      <th>key</th>
      <th>left</th>
      <th>right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_left.merge(df_right,how='left',on='key')
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
      <th>key</th>
      <th>left</th>
      <th>right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_left.merge(df_right,how='right',on='key')
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
      <th>key</th>
      <th>left</th>
      <th>right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>D</td>
      <td>NaN</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



# csv file


```python
%%writefile sea_rain1.csv

연도,동해,남해,서해,전체
1996,17.4629,17.2288,14.436,15.9067
1997,17.4629,17.2288,14.436,15.9067
1998,17.4629,17.2288,14.436,15.9067
1999,17.4629,17.2288,14.436,15.9067
2000,17.4629,17.2288,14.436,15.9067
```

    Overwriting sea_rain1.csv
    


```python
import pandas as pd

pd.read_csv('C:\\Users\\cityo\\Desktop\\datas\\객체\\sea_rain1.csv')
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
      <th>동해</th>
      <th>남해</th>
      <th>서해</th>
      <th>전체</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1996</td>
      <td>17.4629</td>
      <td>17.2288</td>
      <td>14.436</td>
      <td>15.9067</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1997</td>
      <td>17.4629</td>
      <td>17.2288</td>
      <td>14.436</td>
      <td>15.9067</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1998</td>
      <td>17.4629</td>
      <td>17.2288</td>
      <td>14.436</td>
      <td>15.9067</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1999</td>
      <td>17.4629</td>
      <td>17.2288</td>
      <td>14.436</td>
      <td>15.9067</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>17.4629</td>
      <td>17.2288</td>
      <td>14.436</td>
      <td>15.9067</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
