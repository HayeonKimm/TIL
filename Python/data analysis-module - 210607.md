# Module


```python
- 모듈이란 상수,변수,함수,클래스를 포함하는 코드가 저장된 파일이다.

- 모듈로 나누면 코드작성과 관리가 쉬워지고,작성된 코드를 재사용 할 수 있다.
```


```python
#모듈작성은 idle 로 작성한 다음 폴더위치에 저장
```

모듈:


def abdd():

    print('abcccc')



def bbq():
    
    print('ok')




```python
cd C:\Users\cityo\Desktop\python
```

    C:\Users\cityo\Desktop\python



```python
import mo #모듈 이름을 임폴트 한다. (.py를 붙이면 안됌.)
```


```python
print(mo)
```

    <module 'mo' from 'C:\\Users\\cityo\\Desktop\\python\\mo.py'>



```python
mo.abdd() #(모듈 mo에서 abdd 함수를 데려온다.)
```

    abcccc



```python
mo.bbq()
```

    ok

