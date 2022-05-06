# 20210617 엑셀 파일 다루기


```python
import pandas as pd
```


```python
df =pd.read_excel('학생시험성적.xlsx')
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
      <th>학생</th>
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>평균</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>80</td>
      <td>90</td>
      <td>85</td>
      <td>85.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>90</td>
      <td>95</td>
      <td>95</td>
      <td>93.33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>95</td>
      <td>70</td>
      <td>75</td>
      <td>80.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>70</td>
      <td>85</td>
      <td>80</td>
      <td>78.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>75</td>
      <td>90</td>
      <td>85</td>
      <td>83.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_excel('학생시험성적.xlsx',sheet_name=1) #두번째 시트 읽어오기
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
      <th>학생</th>
      <th>과학</th>
      <th>사회</th>
      <th>역사</th>
      <th>평균</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>90</td>
      <td>95</td>
      <td>85</td>
      <td>90.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>85</td>
      <td>90</td>
      <td>80</td>
      <td>85.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>70</td>
      <td>80</td>
      <td>75</td>
      <td>75.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>75</td>
      <td>90</td>
      <td>100</td>
      <td>88.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>90</td>
      <td>80</td>
      <td>90</td>
      <td>86.67</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df=pd.read_excel('학생시험성적.xlsx',sheet_name='2차시험',index_col=0)
df=pd.read_excel('학생시험성적.xlsx',sheet_name='2차시험',index_col='학생') #위와 아래와 같은 결과.칼럼 학생을 인덱스로 교체한다.

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
      <th>과학</th>
      <th>사회</th>
      <th>역사</th>
      <th>평균</th>
    </tr>
    <tr>
      <th>학생</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>90</td>
      <td>95</td>
      <td>85</td>
      <td>90.00</td>
    </tr>
    <tr>
      <th>B</th>
      <td>85</td>
      <td>90</td>
      <td>80</td>
      <td>85.00</td>
    </tr>
    <tr>
      <th>C</th>
      <td>70</td>
      <td>80</td>
      <td>75</td>
      <td>75.00</td>
    </tr>
    <tr>
      <th>D</th>
      <td>75</td>
      <td>90</td>
      <td>100</td>
      <td>88.33</td>
    </tr>
    <tr>
      <th>E</th>
      <td>90</td>
      <td>80</td>
      <td>90</td>
      <td>86.67</td>
    </tr>
  </tbody>
</table>
</div>



# 데이터를 엑셀 파일로 쓰기

방법 세단계  
(1) pandas의 ExcelWriter 객체 생성  
(2) DataFrame 데이터를 지정된 엑셀 시트에 쓰기  
(3) ExcelWriter 객체를 닫고, 지정된 엑셀 파일 생성


```python
# 데이터프레임을 엑셀로 저장하는 예
import pandas as pd

excel_exam_data1 = {'학생':['A','B','C','D','E','F'],
                   '국어':[80,90,95,70,75,80],
                    '영어':[90,95,70,85,90,95],
                    '수학':[85,95,75,80,85,100]}
df1= pd.DataFrame(excel_exam_data1,columns=['학생','국어','영어','수학'])
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
      <th>학생</th>
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>80</td>
      <td>90</td>
      <td>85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>90</td>
      <td>95</td>
      <td>95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>95</td>
      <td>70</td>
      <td>75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>70</td>
      <td>85</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>75</td>
      <td>90</td>
      <td>85</td>
    </tr>
    <tr>
      <th>5</th>
      <td>F</td>
      <td>80</td>
      <td>95</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
excel_writer=pd.ExcelWriter('학생시험성적2.xlsx',engine='xlsxwriter')
df1.to_excel(excel_writer,index=False)
excel_writer.save()  #datas에 저장완료
```

# 엑셀 통합하기


```python
excel_data_files=['담당자별_판매량_Andy사원.xlsx',
                 '담당자별_판매량_Becky사원.xlsx',
                 '담당자별_판매량_Chris사원.xlsx']
```


```python
total_data=pd.DataFrame() #통합을 위해 데이터프레임 형태로 변수를 하나 생성
```


```python
# import pandas as pd

for i in excel_data_files:
    df=pd.read_excel(i)
    total_data=total_data.append(df)
    
total_data
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
      <th>제품명</th>
      <th>담당자</th>
      <th>지역</th>
      <th>1분기</th>
      <th>2분기</th>
      <th>3분기</th>
      <th>4분기</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>시계</td>
      <td>A</td>
      <td>가</td>
      <td>198</td>
      <td>123</td>
      <td>120</td>
      <td>137</td>
    </tr>
    <tr>
      <th>1</th>
      <td>구두</td>
      <td>A</td>
      <td>가</td>
      <td>273</td>
      <td>241</td>
      <td>296</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>핸드백</td>
      <td>A</td>
      <td>가</td>
      <td>385</td>
      <td>316</td>
      <td>355</td>
      <td>331</td>
    </tr>
    <tr>
      <th>0</th>
      <td>시계</td>
      <td>B</td>
      <td>나</td>
      <td>154</td>
      <td>108</td>
      <td>155</td>
      <td>114</td>
    </tr>
    <tr>
      <th>1</th>
      <td>구두</td>
      <td>B</td>
      <td>나</td>
      <td>200</td>
      <td>223</td>
      <td>213</td>
      <td>202</td>
    </tr>
    <tr>
      <th>2</th>
      <td>핸드백</td>
      <td>B</td>
      <td>나</td>
      <td>350</td>
      <td>340</td>
      <td>377</td>
      <td>392</td>
    </tr>
    <tr>
      <th>0</th>
      <td>시계</td>
      <td>C</td>
      <td>다</td>
      <td>168</td>
      <td>102</td>
      <td>149</td>
      <td>174</td>
    </tr>
    <tr>
      <th>1</th>
      <td>구두</td>
      <td>C</td>
      <td>다</td>
      <td>231</td>
      <td>279</td>
      <td>277</td>
      <td>292</td>
    </tr>
    <tr>
      <th>2</th>
      <td>핸드백</td>
      <td>C</td>
      <td>다</td>
      <td>365</td>
      <td>383</td>
      <td>308</td>
      <td>323</td>
    </tr>
  </tbody>
</table>
</div>




```python
# import pandas as pd 

for i in excel_data_files:
    df=pd.read_excel(i)
    total_data=total_data.append(df,ignore_index=True)  #그대로 가지고 온 인덱스를 숫자에 맞게 배열
    
total_data   
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
      <th>제품명</th>
      <th>담당자</th>
      <th>지역</th>
      <th>1분기</th>
      <th>2분기</th>
      <th>3분기</th>
      <th>4분기</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>시계</td>
      <td>A</td>
      <td>가</td>
      <td>198</td>
      <td>123</td>
      <td>120</td>
      <td>137</td>
    </tr>
    <tr>
      <th>1</th>
      <td>구두</td>
      <td>A</td>
      <td>가</td>
      <td>273</td>
      <td>241</td>
      <td>296</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>핸드백</td>
      <td>A</td>
      <td>가</td>
      <td>385</td>
      <td>316</td>
      <td>355</td>
      <td>331</td>
    </tr>
    <tr>
      <th>3</th>
      <td>시계</td>
      <td>B</td>
      <td>나</td>
      <td>154</td>
      <td>108</td>
      <td>155</td>
      <td>114</td>
    </tr>
    <tr>
      <th>4</th>
      <td>구두</td>
      <td>B</td>
      <td>나</td>
      <td>200</td>
      <td>223</td>
      <td>213</td>
      <td>202</td>
    </tr>
    <tr>
      <th>5</th>
      <td>핸드백</td>
      <td>B</td>
      <td>나</td>
      <td>350</td>
      <td>340</td>
      <td>377</td>
      <td>392</td>
    </tr>
    <tr>
      <th>6</th>
      <td>시계</td>
      <td>C</td>
      <td>다</td>
      <td>168</td>
      <td>102</td>
      <td>149</td>
      <td>174</td>
    </tr>
    <tr>
      <th>7</th>
      <td>구두</td>
      <td>C</td>
      <td>다</td>
      <td>231</td>
      <td>279</td>
      <td>277</td>
      <td>292</td>
    </tr>
    <tr>
      <th>8</th>
      <td>핸드백</td>
      <td>C</td>
      <td>다</td>
      <td>365</td>
      <td>383</td>
      <td>308</td>
      <td>323</td>
    </tr>
    <tr>
      <th>9</th>
      <td>시계</td>
      <td>A</td>
      <td>가</td>
      <td>198</td>
      <td>123</td>
      <td>120</td>
      <td>137</td>
    </tr>
    <tr>
      <th>10</th>
      <td>구두</td>
      <td>A</td>
      <td>가</td>
      <td>273</td>
      <td>241</td>
      <td>296</td>
      <td>217</td>
    </tr>
    <tr>
      <th>11</th>
      <td>핸드백</td>
      <td>A</td>
      <td>가</td>
      <td>385</td>
      <td>316</td>
      <td>355</td>
      <td>331</td>
    </tr>
    <tr>
      <th>12</th>
      <td>시계</td>
      <td>B</td>
      <td>나</td>
      <td>154</td>
      <td>108</td>
      <td>155</td>
      <td>114</td>
    </tr>
    <tr>
      <th>13</th>
      <td>구두</td>
      <td>B</td>
      <td>나</td>
      <td>200</td>
      <td>223</td>
      <td>213</td>
      <td>202</td>
    </tr>
    <tr>
      <th>14</th>
      <td>핸드백</td>
      <td>B</td>
      <td>나</td>
      <td>350</td>
      <td>340</td>
      <td>377</td>
      <td>392</td>
    </tr>
    <tr>
      <th>15</th>
      <td>시계</td>
      <td>C</td>
      <td>다</td>
      <td>168</td>
      <td>102</td>
      <td>149</td>
      <td>174</td>
    </tr>
    <tr>
      <th>16</th>
      <td>구두</td>
      <td>C</td>
      <td>다</td>
      <td>231</td>
      <td>279</td>
      <td>277</td>
      <td>292</td>
    </tr>
    <tr>
      <th>17</th>
      <td>핸드백</td>
      <td>C</td>
      <td>다</td>
      <td>365</td>
      <td>383</td>
      <td>308</td>
      <td>323</td>
    </tr>
  </tbody>
</table>
</div>




```python
# import pandas as pd 
import glob


excel_file_name='담당자별_판매량_통합'


excel_data_files1=glob.glob("담당자별_판매량_*사원.xlsx")
total_data1=pd.DataFrame()


for f in excel_data_files1:
    df = pd.read_excel(f)
    total_data1 = total_data1.append(df,ignore_index=True)

excel_total_file_writer = pd.ExcelWriter(excel_file_name,engine='xlsxwriter')
total_data1.to_excel(excel_total_file_writer,index=False,sheet_name='담당자별_판매량_통합')

excel_total_file_writer.save()


glob.glob(excel_file_name)   
```




    ['담당자별_판매량_통합']




```python
import glob   # 엑셀 이름 모두를 쓰지않고 불러오는 방법

glob.glob('담당자별_판매량*사원.xlsx')
```




    ['담당자별_판매량_Andy사원.xlsx', '담당자별_판매량_Becky사원.xlsx', '담당자별_판매량_Chris사원.xlsx']



# 엑셀 값 바꾸기


```python
df = pd.read_excel('학생시험성적.xlsx')
df.loc[2,'국어']=99
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
      <th>학생</th>
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>평균</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>80</td>
      <td>90</td>
      <td>85</td>
      <td>85.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>90</td>
      <td>95</td>
      <td>95</td>
      <td>93.33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>99</td>
      <td>70</td>
      <td>75</td>
      <td>80.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>70</td>
      <td>85</td>
      <td>80</td>
      <td>78.33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>75</td>
      <td>90</td>
      <td>85</td>
      <td>83.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[5,'국사']=99
df.loc[6,'국마']=99
df.loc[6,'국머']=99
df.loc[7,'국자']=99
df.loc[8,'국카']=99
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
      <th>학생</th>
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>평균</th>
      <th>국사</th>
      <th>국마</th>
      <th>국머</th>
      <th>국자</th>
      <th>국카</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>80.0</td>
      <td>90.0</td>
      <td>85.0</td>
      <td>85.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>90.0</td>
      <td>95.0</td>
      <td>95.0</td>
      <td>93.33</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>99.0</td>
      <td>70.0</td>
      <td>75.0</td>
      <td>80.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>70.0</td>
      <td>85.0</td>
      <td>80.0</td>
      <td>78.33</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>75.0</td>
      <td>90.0</td>
      <td>85.0</td>
      <td>83.33</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.0</td>
      <td>99.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['학생']='F'
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
      <th>학생</th>
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>평균</th>
      <th>국사</th>
      <th>국마</th>
      <th>국머</th>
      <th>국자</th>
      <th>국카</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>80.0</td>
      <td>90.0</td>
      <td>85.0</td>
      <td>85.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>90.0</td>
      <td>95.0</td>
      <td>95.0</td>
      <td>93.33</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>99.0</td>
      <td>70.0</td>
      <td>75.0</td>
      <td>80.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>70.0</td>
      <td>85.0</td>
      <td>80.0</td>
      <td>78.33</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>75.0</td>
      <td>90.0</td>
      <td>85.0</td>
      <td>83.33</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>F</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>F</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.0</td>
      <td>99.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>F</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>F</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.0</td>
    </tr>
  </tbody>
</table>
</div>



# 엑셀 필터기능


```python
df = pd.read_excel('담당자별_판매량_통합')
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
      <th>제품명</th>
      <th>담당자</th>
      <th>지역</th>
      <th>1분기</th>
      <th>2분기</th>
      <th>3분기</th>
      <th>4분기</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>시계</td>
      <td>A</td>
      <td>가</td>
      <td>198</td>
      <td>123</td>
      <td>120</td>
      <td>137</td>
    </tr>
    <tr>
      <th>1</th>
      <td>구두</td>
      <td>A</td>
      <td>가</td>
      <td>273</td>
      <td>241</td>
      <td>296</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>핸드백</td>
      <td>A</td>
      <td>가</td>
      <td>385</td>
      <td>316</td>
      <td>355</td>
      <td>331</td>
    </tr>
    <tr>
      <th>3</th>
      <td>시계</td>
      <td>B</td>
      <td>나</td>
      <td>154</td>
      <td>108</td>
      <td>155</td>
      <td>114</td>
    </tr>
    <tr>
      <th>4</th>
      <td>구두</td>
      <td>B</td>
      <td>나</td>
      <td>200</td>
      <td>223</td>
      <td>213</td>
      <td>202</td>
    </tr>
    <tr>
      <th>5</th>
      <td>핸드백</td>
      <td>B</td>
      <td>나</td>
      <td>350</td>
      <td>340</td>
      <td>377</td>
      <td>392</td>
    </tr>
    <tr>
      <th>6</th>
      <td>시계</td>
      <td>C</td>
      <td>다</td>
      <td>168</td>
      <td>102</td>
      <td>149</td>
      <td>174</td>
    </tr>
    <tr>
      <th>7</th>
      <td>구두</td>
      <td>C</td>
      <td>다</td>
      <td>231</td>
      <td>279</td>
      <td>277</td>
      <td>292</td>
    </tr>
    <tr>
      <th>8</th>
      <td>핸드백</td>
      <td>C</td>
      <td>다</td>
      <td>365</td>
      <td>383</td>
      <td>308</td>
      <td>323</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['제품명']
```




    0     시계
    1     구두
    2    핸드백
    3     시계
    4     구두
    5    핸드백
    6     시계
    7     구두
    8    핸드백
    Name: 제품명, dtype: object




```python
df['제품명']='핸드볼'
df['제품명']=='핸드백'

```




    0    False
    1    False
    2    False
    3    False
    4    False
    5    False
    6    False
    7    False
    8    False
    Name: 제품명, dtype: bool




```python
handbag=df[df['제품명']=='핸드백']
handbag
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
      <th>제품명</th>
      <th>담당자</th>
      <th>지역</th>
      <th>1분기</th>
      <th>2분기</th>
      <th>3분기</th>
      <th>4분기</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
handbag=df[df['제품명']=='핸드볼']
handbag
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
      <th>제품명</th>
      <th>담당자</th>
      <th>지역</th>
      <th>1분기</th>
      <th>2분기</th>
      <th>3분기</th>
      <th>4분기</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>핸드볼</td>
      <td>A</td>
      <td>가</td>
      <td>198</td>
      <td>123</td>
      <td>120</td>
      <td>137</td>
    </tr>
    <tr>
      <th>1</th>
      <td>핸드볼</td>
      <td>A</td>
      <td>가</td>
      <td>273</td>
      <td>241</td>
      <td>296</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>핸드볼</td>
      <td>A</td>
      <td>가</td>
      <td>385</td>
      <td>316</td>
      <td>355</td>
      <td>331</td>
    </tr>
    <tr>
      <th>3</th>
      <td>핸드볼</td>
      <td>B</td>
      <td>나</td>
      <td>154</td>
      <td>108</td>
      <td>155</td>
      <td>114</td>
    </tr>
    <tr>
      <th>4</th>
      <td>핸드볼</td>
      <td>B</td>
      <td>나</td>
      <td>200</td>
      <td>223</td>
      <td>213</td>
      <td>202</td>
    </tr>
    <tr>
      <th>5</th>
      <td>핸드볼</td>
      <td>B</td>
      <td>나</td>
      <td>350</td>
      <td>340</td>
      <td>377</td>
      <td>392</td>
    </tr>
    <tr>
      <th>6</th>
      <td>핸드볼</td>
      <td>C</td>
      <td>다</td>
      <td>168</td>
      <td>102</td>
      <td>149</td>
      <td>174</td>
    </tr>
    <tr>
      <th>7</th>
      <td>핸드볼</td>
      <td>C</td>
      <td>다</td>
      <td>231</td>
      <td>279</td>
      <td>277</td>
      <td>292</td>
    </tr>
    <tr>
      <th>8</th>
      <td>핸드볼</td>
      <td>C</td>
      <td>다</td>
      <td>365</td>
      <td>383</td>
      <td>308</td>
      <td>323</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
