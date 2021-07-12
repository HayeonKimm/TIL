# 데이터분석 210607
- 파일읽고 처리하기 


```python

```


```python

```


```python
file_name = 'C:/Users/cityo/Desktop/python/CoffeeShopSales.txt'
```


```python
f = open(file_name)


for line in f:
    print(line,end ='')
f.close()
```

    date        espresso    americano   cafelatte  cappicino
    10.15        14             18           29          20
    10.16        12             45           41          18
    10.17        11             53           32          25
    10.18        15             49           38          22
    


```python

```


```python
f = open(file_name)
header = f.readline()
```


```python
f.close()
header
```




    'date        espresso    americano   cafelatte  cappicino\n'




```python
f = open(file_name)
header = f.readline()
headerList= header.split()

espresso =[]
americano =[]
cafelatte=[]
cappucino=[]

for line in f:
    dataList =line.split()
    
    espresso.append(int(dataList[1]))
    americano.append(int(dataList[2]))
    cafelatte.append(int(dataList[3]))
    cappucino.append(int(dataList[4]))
    
f.close()

print("{0}:{1}".format(headerList[1],espresso))
print("{0}:{1}".format(headerList[2],americano))
print("{0}:{1}".format(headerList[3],cafelatte))
print("{0}:{1}".format(headerList[4],cappucino))
```

    espresso:[14, 12, 11, 15]
    americano:[18, 45, 53, 49]
    cafelatte:[29, 41, 32, 38]
    cappicino:[20, 18, 25, 22]
    


```python
total_sum = [sum(espresso),sum(americano),sum(cafelatte),sum(cappucino)]
total_mean= [sum(espresso)/len(espresso),sum(americano)/len(americano),sum(cafelatte)/len(cafelatte),sum(cappucino)/len(cappucino)]
```


```python
for k in range(len(total_sum)):
    print('[{0}]판매량'.format(headerList[k+1]))
    print('전체 판매량:{0}, 하루 평균 판매량 :{1}'.format(total_sum[k],total_mean[k]))
```

    [espresso]판매량
    전체 판매량:52, 하루 평균 판매량 :13.0
    [americano]판매량
    전체 판매량:165, 하루 평균 판매량 :41.25
    [cafelatte]판매량
    전체 판매량:140, 하루 평균 판매량 :35.0
    [cappicino]판매량
    전체 판매량:85, 하루 평균 판매량 :21.25
    


```python

```
