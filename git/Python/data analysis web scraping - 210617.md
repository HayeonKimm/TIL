# Web Scraping : 
###  컴퓨터 소프트웨어 기술을 활용해 웹 사이트내에 있는 정보를 추출하는 것.

## 웹사이트 접속


```python
import webbrowser   

url = 'www.naver.net'
webbrowser.open(url)
```




    True




```python
import webbrowser

naver_search_url = "http://search.naver.com/search.naver?query="
search_word='파이썬'

url = naver_search_url+search_word

webbrowser.open_new(url)
```




    True



## 여러개 웹 사이트 접속


```python
# import webbrowser

urls= ['www.naver.com','www.daum.net','www.google.com']

for url in urls:
    webbrowser.open_new(url)
```


```python
import webbrowser

google_url = "www.google.com/#q="
search_words = ['python web scraping', 'python webbrowser']

for search_word in search_words:
    webbrowser.open_new(google_url + search_word)
```

### 위의 내용은 검색어를 찾는게 안된다. 왜그런지 모르겠다. 


```python
import webbrowser

google_url = "https://www.google.com/search?q="
search_words = ['python web scraping', 'python webbrowser']

for search_word in search_words:
    webbrowser.open_new(google_url + search_word)


# https://www.google.com/search?q=
```

### 구글 search url 을 새로 찾아넣으니 해결되었다.

# html 기본지식


```python
%%writefile HTML_example.html


<!doctype html>

<html>

<head>
<meta charset = "utf-8">
<title>김하연최고</title>


</head>

<body>

<p> 하연 </p>
<p> 하연님 </p>
<p> 김김김 </p>

</body>



</html>
```

    Overwriting HTML_example.html
    

id와 같은 태그의 속성은 웹 페이지에서 특정 데이터를 추출할 때 아주 중요한 정보.  
이 속성을 이용하면 손쉽게 원하는 데이터를 획득가능.

## 웹페이지의 HTML 소스 가져오기, 분석, 처리


```python
import requests

r = requests.get("http://www.google.co.kr")
r                   # 응답이 잘 됐다면 <Response [200] 을 보여준다.
```




    <Response [200]>




```python
r.text[0:100]   # r.text를 쓰면 소스코드 전체를 보여주기 때문에, 인덱싱으로 조금만.
```




    '<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content'




```python
from bs4 import BeautifulSoup

# 테스트용 html 코드
html = """<html><body><div><span>\
        <a href=http://www.naver.com>naver</a>\
        <a href=https://www.google.com>google</a>\
        <a href=http://www.daum.net/>daum</a>\
        </span></div></body></html>""" 

# BeautifulSoup를 이용해 HTML 소스를 파싱
soup = BeautifulSoup(html, 'lxml')  # lxml은 소스를 처리하기 위한 파서 
soup
```




    <html><body><div><span> <a href="http://www.naver.com">naver</a> <a href="https://www.google.com">google</a> <a href="http://www.daum.net/">daum</a> </span></div></body></html>




```python
print(soup.prettify()) # 좀 더 정돈되서 보기
```

    <html>
     <body>
      <div>
       <span>
        <a href="http://www.naver.com">
         naver
        </a>
        <a href="https://www.google.com">
         google
        </a>
        <a href="http://www.daum.net/">
         daum
        </a>
       </span>
      </div>
     </body>
    </html>
    


```python
soup.find('www') # 원하는 부분 찾기
```

### 또 안된다


```python
soup.find('a') # 글자가 아니라 태그였다.
```




    <a href="http://www.naver.com">naver</a>




```python
soup.find('a').get_text() # 태그말고 텍스트만 추출할 때
```




    'naver'




```python
soup.find_all('a') #a 태그 있는거 다 가져오긴
```




    [<a href="http://www.naver.com">naver</a>,
     <a href="https://www.google.com">google</a>,
     <a href="http://www.daum.net/">daum</a>]




```python
site_names = soup.find_all('a')
for site_name in site_names:
    print(site_name.get_text())   #get_text()는 리스트에 적용할 수 없으므로 for문을 이용, find_all이 안된다.
```

    naver
    google
    daum
    

## 다른 예시


```python
from bs4 import BeautifulSoup

# 테스트용 HTML 코드
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
 </body>
</html>
""" 

soup2 = BeautifulSoup(html2, "lxml")
```


```python
soup2.title # 타이틀 가져오기
```




    <title>작품과 작가 모음</title>




```python
soup2.head #헤드
```




    <head>
    <title>작품과 작가 모음</title>
    </head>




```python
soup2.body #바디
```




    <body>
    <h1>책 정보</h1>
    <p id="book_title">토지</p>
    <p id="author">박경리</p>
    <p id="book_title">태백산맥</p>
    <p id="author">조정래</p>
    <p id="book_title">감옥으로부터의 사색</p>
    <p id="author">신영복</p>
    </body>




```python
soup2.body.h1
```




    <h1>책 정보</h1>



### 속성값 이용해서 찾기


```python
soup2.find('p',{"id":"book_title"})
# book_title = 속성값, 속성값을 갖는 '*첫번째* 요소'
```




    <p id="book_title">토지</p>




```python
soup2.find_all('p',{"id":"book_title"}) # book_title 전체찾기
```




    [<p id="book_title">토지</p>,
     <p id="book_title">태백산맥</p>,
     <p id="book_title">감옥으로부터의 사색</p>]



# 총 정리


```python
from bs4 import BeautifulSoup

soup2 = BeautifulSoup(html2,"lxml")

book_titles = soup2.find_all('p', {"id":"book_title"})
authors = soup2.find_all('p', {"id":"author"})

for book_title, author in zip(book_titles, authors):
    
    print(book_title.get_text() +'/'+ author.get_text())
```

    토지/박경리
    태백산맥/조정래
    감옥으로부터의 사색/신영복
    


```python

```
