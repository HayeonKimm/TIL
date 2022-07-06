> npx artillery quick --count 100 -n 50 http://localhost:3000

--count 옵션은 가상의 사용자 수를 의미하고,
-n 옵션은 요청 횟수를 의미한다.
--rate 옵션은 초당 요청을 의미한다.


npx artillery run loadtest.json

좀 더 상세한 옵션에 대한 내용을 보고 싶다면 artillery quick -h 를 통해 확인 할 수 있다.
출처: https://inpa.tistory.com/entry/JEST-📚-부하-테스트-Stress-Test [👨‍💻 Dev Scroll:티스토리]



