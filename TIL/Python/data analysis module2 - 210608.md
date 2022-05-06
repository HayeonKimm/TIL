# Module 2

- idle 로 모듈작성


```python
# PI=3.14

# def square_area(a):
#     return a**2

# def circle_area(r):
#     return PI *r **2
```


```python

```


```python
cd C:\Users\cityo\Desktop\python2
```

    C:\Users\cityo\Desktop\python2
    


```python
import myarea
```


```python
print('pi=',myarea.PI)
print('square area=',myarea.square_area(5))
print('circle area=',myarea.circle_area(2))
```

    pi= 3.14
    square area= 25
    circle area= 12.56
    


```python

```


```python
dir(myarea) # 불러온 모듈에서 사용할 수 있는 변수, 함수 ,클래스를 알고 싶으면 dir(모듈명) 을 이용
```




    ['PI',
     '__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'circle_area',
     'square_area']




```python

```

## 모듈을 불러오는 다른 형식 

#### from 모듈명 import 변수명
#### from 모듈명 import 함수명
#### from 모듈명 import 클래스명

## 모듈명을 별명으로 선언

### from 모듈명 import 변수명 as 별명


```python

```

# 모듈을 직접 실행하는 경우와 임포트한 후 실행하는 경우 구분하기


```python
#모듈
```


```python


# def func(a):
#     print('입력 숫자:',a)



# func(3)

```


```python

```


```python
%run C:\Users\cityo\Desktop\python2\mymodule
```

    입력 숫자: 3
    


```python

```


```python
import mymodule
```

    입력 숫자: 3
    


```python

```


```python

```

# if __name__= "__main__":

## 같은 모듈에서 코드를 직접 수행할 때만 'if __name__= "__main__":' 이 실행되고 아닌 경우는 실행되지 않음.


```python

```


```python
#예시

# def func(a):
#     print("입력 숫자:",a)
    
# if __name__ ="__main__":
#     print("모듈을 직접 실행")
#     func(3)
#     func(4)
    
# else:
#     print(:모듈을 임포트해서 실행")
```


```python
%run C:\Users\cityo\Desktop\python2\module2.py   #직접 실행하면 코드가 수행된다.
```

    모듈을 직접 실행
    입력 숫자: 3
    입력 숫자: 4
    


```python

```


```python
import module2
```

    모듈을 임포트해서 실행
    


```python

```

# 난수발생 모듈


```python
import random

random.random()   #0~1사이의 임의의 실수를 발생시키는 random()함수
```




    0.5386283661201378



random()    
randint(a,b)  a<=정수<=b 의 범위의 임의의 정수 반환  
randrange([start,],stop[,step])  range([start,]stop[,step])에서 임의의 정수 반환  
choice(seq) 공백이 아닌 시퀀스(seq)에서 임의의 항목을 반환  
sample(population,k) 시퀀스로 이뤄진 모집단(population)에서 중복이 되지 않는 k개의 인자를 반환


```python
import random

random.randrange(0,11,2)
```




    2




```python
num1 =random.randrange(1,10,2) #홀수 발생 시킬 떄 
```


```python
num1
```




    3




```python
num2 =random.randrange(0,11,2) #짝수 발생 시킬 때
```


```python
num2
```




    4




```python

```

# 날짜 및 시간 관련 모듈


```python
import datetime

set_day= datetime.date(2019,3,1)
```


```python
set_day
```




    datetime.date(2019, 3, 1)




```python
print(set_day)
```

    2019-03-01
    


```python
print('{0}/{1}/{2}'.format(set_day.year,set_day.month,set_day.day))
```

    2019/3/1
    


```python

```
