# Data analysis web scraping2 - 210618


```python
%%writefile HTML_example_my_site.html

<!doctype html>
<html>

<head>
<meta charset='utf-8'>

<title>사이트 모_음_김하연</title>
</head>

<body>

<p id="title"><b>자주 가는 사이트 모음_김하연 </b></p>
<p id="content">이곳은 자주 가는 사이트를 모아둔 곳입니다.</p>
<a href="http://www.naver.com" class ="portal" id ="naver"> 네이버 </a> <br>
<a href="http://www.google.com" class = "search" id ="google">구글 </a> <br>
<a href="http://daum.net" class="portal" id ="daum">다음</a> <br>
<a href="http://nl.go.kr" class="goverment" id="nl">국립중앙도서관</a> <br>  #<br>은 줄바꿈기능
<a href="http://daum.tistory.net" class = "blog" id ="tistoty">티스토리</a> <br> #이건 임의대로 추가


</body>

</html>
```

    Overwriting HTML_example_my_site.html
    


```python
from bs4 import BeautifulSoup


f = open("HTML_example_my_site.html",encoding='utf-8')

html3=f.read()
f.close()

soup3 = BeautifulSoup(html3,"lxml") 
```


```python
soup3.select('a') # 태그가 a인것 가져오기
```




    [<a class="portal" href="http://www.naver.com" id="naver"> 네이버 </a>,
     <a class="search" href="http://www.google.com" id="google">구글 </a>,
     <a class="portal" href="http://daum.net" id="daum">다음</a>,
     <a class="goverment" href="http://nl.go.kr" id="nl">국립중앙도서관</a>,
     <a class="blog" href="http://daum.tistory.net" id="tistoty">티스토리</a>]




```python
soup3.select('a.portal') #태그가 a이면서 class속성값이 portal 인 요소만 가져오기
```




    [<a class="portal" href="http://www.naver.com" id="naver"> 네이버 </a>,
     <a class="portal" href="http://daum.net" id="daum">다음</a>]



## 웹브라우저의 요소 검사기능
### : HTML 소스코드는 대부분 길고 복잡해서 눈으로 확인하면서 분석하기가 쉽지 않다. 요소기능 검사기능을 이용하면 좀 더 쉽게 분석 할 수 있다.

- 웹 브라우저로 요소 검사를 원하는 웹 사이트에 접속한다.
- 웹 사이트 화면의 관심 위치로 마우스 커서를 옮기고 마우스 오른쪽 버튼을 클릭한다.
- 크롬은 [검사]를 마우스로 클릭한다.

## 가독성 챙기기


```python
%%writefile br_example_constitution.html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>줄 바꿈 테스트 예제</title>
  </head>
  <body>
  <p id="title"><b>대한민국헌법</b></p>
  <p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>
  <p id="content">제2조 <br/>①대한민국의 국민이 되는 요건은 법률로 정한다.<br/>②국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다.</p>
  </body>
</html>
```

    Writing br_example_constitution.html
    


```python
from bs4 import BeautifulSoup

f = open('br_example_constitution.html', encoding='utf-8')

html_source = f.read()
f.close()

soup = BeautifulSoup(html_source, "lxml")

title = soup.find('p', {"id":"title"})
contents = soup.find_all('p', {"id":"content"})

print(title.get_text())
for content in contents:
    print(content.get_text())
```

    대한민국헌법
    제1조 ①대한민국은 민주공화국이다.②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.
    제2조 ①대한민국의 국민이 되는 요건은 법률로 정한다.②국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다.
    

### br태그를 \n태그로 교체하면 된다.


```python
soup2 = BeautifulSoup(html1, "lxml")
content2 = soup2.find('p', {"id":"content"})

br_contents = content2.find_all("br")
for br_content in br_contents:
    br_content.replace_with("\n")
print(content2)
```

    <p id="content">제1조 
    ①대한민국은 민주공화국이다.
    ②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>
    

### 이 기능을 함수로 만들기


```python
def replace_newline(soup_html):
    br_to_newlines = soup_html.find_all("br")
    for br_to_newline in br_to_newlines: 
        br_to_newline.replace_with("\n")
    return soup_html
```


```python
soup2 = BeautifulSoup(html1, "lxml")
content2 = soup2.find('p', {"id":"content"})
content3 = replace_newline(content2)
print(content3.get_text()) #이 줄은 텍스트만을 뽑아내기 위해서. get_text()
```

    제1조 
    ①대한민국은 민주공화국이다.
    ②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.
    


```python

```
