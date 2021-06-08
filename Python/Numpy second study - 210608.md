# Numpy 두번쨰


```python
import numpy as np
```


```python
str_a1 =np.array(['1.567','0.123','5.123'])           # 문자열로 구성된 NUMPY 배열의 모든 원소를 정수나 실수로 변환 가능하다.
num_a1 =str_a1.astype(float)
```


```python
num_a1
```




    array([1.567, 0.123, 5.123])




```python
str_a1
```




    array(['1.567', '0.123', '5.123'], dtype='<U5')




```python
str_a1.dtype
```




    dtype('<U5')




```python
num_a1.dtype
```




    dtype('float64')




```python

```


```python
num_f1 = np.array([10,21,0.579,4.75]) #실수를 정수로 변환
```


```python
num_i1 = num_f1.astype(int)
num_i1
```




    array([10, 21,  0,  4])




```python

```

## 배열의 연산 - 기본연산


```python
arr1 = np.array([10,20,30,40])
arr2 = np.array([1,2,3,4])
```


```python
arr1+arr2
```




    array([11, 22, 33, 44])




```python
arr1-arr2
```




    array([ 9, 18, 27, 36])




```python
arr1*2
```




    array([20, 40, 60, 80])




```python
arr1 *arr2
```




    array([ 10,  40,  90, 160])




```python
arr1 /arr2
```




    array([10., 10., 10., 10.])




```python
arr1 >2
```




    array([ True,  True,  True,  True])




```python
arr1 <2
```




    array([False, False, False, False])




```python

```


```python

```


```python
[arr1.sum(),arr2.mean()]
```




    [100, 2.5]




```python
# std()=표준편차
# var()=분산
# mean()=평균
# sum()=총계

```


```python
[arr1.std(),arr1.var()]
```




    [11.180339887498949, 125.0]




```python
[arr1.min(),arr1.max()]
```




    [10, 40]




```python

```


```python
arr3=np.arange(1,5)
```


```python
arr3
```




    array([1, 2, 3, 4])




```python
arr3.cumsum() #누적합
```




    array([ 1,  3,  6, 10], dtype=int32)




```python
arr3.cumprod() #누적곱
```




    array([ 1,  2,  6, 24], dtype=int32)




```python

```

## 행렬연산


```python
A = np.array([0,1,2,3]).reshape(2,2)
```


```python
A
```




    array([[0, 1],
           [2, 3]])




```python
B = np.array([4,3,5,5]).reshape(2,2)
```


```python
B
```




    array([[4, 3],
           [5, 5]])




```python
A.dot(B)
```




    array([[ 5,  5],
           [23, 21]])




```python
B.dot(A)
```




    array([[ 6, 13],
           [10, 20]])




```python
np.dot(A,B)  # A.dot(B)와 동일
```




    array([[ 5,  5],
           [23, 21]])




```python
np.transpose(A) #전치행렬
```




    array([[0, 2],
           [1, 3]])




```python

```


```python
np.linalg.inv(A)  #역행렬
```




    array([[-1.5,  0.5],
           [ 1. ,  0. ]])



## 인덱싱


```python
a1= np.array([0,1,2,3,4,5,10,20,30])
```


```python
a1[0], a1[5]
```




    (0, 5)




```python
a1[0]=1 #바꾸기
```


```python
a1
```




    array([ 1,  1,  2,  3,  4,  5, 10, 20, 30])




```python
a1[[1,2,4,6]] #배열에서 여러개 원소를 선택하기.
```




    array([ 1,  2,  4, 10])




```python

```


```python
a2= np.arange(10,100,10).reshape(3,3)
```


```python
a2
```




    array([[10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]])




```python
a2[0,2] #행의 위치가 0이고 열의 위치가 2인 원소
```




    30




```python
a2[1] #행 전체를 가져오는 방법
```




    array([40, 50, 60])




```python
a2[1]= [30,30,1] #행 전체 바꾸기
```


```python
a2
```




    array([[10, 20, 30],
           [30, 30,  1],
           [70, 80, 90]])




```python
a= np.array([1,2,3,4,5,6])  #원소중에서 3보다 큰 원소만 가져오는 방법
a[a>3]
```




    array([4, 5, 6])




```python
a[(a%2)]
```




    array([2, 1, 2, 1, 2, 1])



### 슬라이싱


```python
b1 = np.array([0,10,20,30,40,60])
```


```python
b1[0:4]
```




    array([ 0, 10, 20, 30])




```python
b2= np.arange(10,100,10).reshape(3,3)
```


```python
b2
```




    array([[10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]])




```python
b2[1:3,1:3]
```




    array([[50, 60],
           [80, 90]])




```python
b2[:3,1:]
```




    array([[20, 30],
           [50, 60],
           [80, 90]])




```python
b2[1][0:2]
```




    array([40, 50])




```python
b2[0:2,1:3] =np.array([[25,35],[55,65]])
```


```python
b2
```




    array([[10, 25, 35],
           [40, 55, 65],
           [70, 80, 90]])




```python

```
