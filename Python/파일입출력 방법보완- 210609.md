# 파일 입출력


```python
%%writefile kim.py

a = 1
_a = 2
__a = 3

def b():
    return 1

def _b():
    return 2

def __b():
    return 3
```

    Writing kim.py
    


```python
import kim     # 파일을 임포트
                # python은 파일도 객체
            
```


```python
kim.a
```




    1




```python
kim._a
```




    2




```python
kim.__a
```




    3




```python

```
