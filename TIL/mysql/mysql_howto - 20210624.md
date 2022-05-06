### 스스로 실습해보기
### orderNumber 10000이상 10101 이하 값 가져오기  

select *    
from classicmodels.orderdetails                           
where 10000< orderNumber < 10101	
  
		
  
  		
  		
  		
  	
### employees 테이블에서 lastname이 murphy 인 사람만 데려오기 				

select *  
from classicmodels.employees  
where lastname = 'murphy';</p> 

<p></p>

### payment 테이블에서 paymentdate가 20050501일 이후이며, 봉급이 10000.0이 넘는사람만 가져오기


select *  
from classicmodels.payments  
where paymentDate > 20050501  
and amount > 10000.0;  



###  in 기능 사용해보기 



select *  
from customers  
where city in ('madrid');  





### like 기능

select *  
from customers  
where city like 'mad___';  



### like 기능중 % 기능

select *  
from customers  
where city like 'new%'  

### city 중 컨택트퍼스트네임이 캐린인 시티의 칼럼만 가져오기

select *  
from customers  
where city = (	select city  
				from customers  
				where contactfirstname= 'carine');  
           
	   
	   
	   

### any : 서브쿼리에서 해당되는 경우가 여러가지일때 모두 가져오게 해주는 명령어



### dsc 내림차순으로 정리 , asc 오름차순.

select *  
from classicmodels.payments  
where paymentDate > 20050501  
and amount > 10000.0   
order by amount asc;  



### employees 테이블에서 officecode 5이상인 데이터만 employeenumber desc순으로 나열한다.

select *  
from classicmodels.employees  
where officecode > 5  
order by employeenumber desc;  


select CountryCode, MAX(Population)  
from world.city  
group by countryCode;  

select CountryCode, min(Population)  
from world.city  
group by countryCode;  

select CountryCode, min(Population) as 'average'  
from world.city  
group by countryCode;  





### city table의 전체 개수를 구하면 city의 수를 알 수 있다.

select count(*)  
from city  





### 평균인구수

select avg(population)  
from city  





### having은 집계함수에서 조건을 달때 쓴다.

select countrycode, max(population)  
from city  
group by countrycode  
having max(population)>8000000  





### rollup : 총합 또는 중간합계가 필요한 경우

select countrycode, name ,sum(population)  
from city  
group by countrycode, name with rollup;  

<p></p>
<p></p>
<p></p>
<p></p>
### join

### 세개의 테이블이 합친 예시. 이건 좀 어렵다.

select *  
from city  
join country on city.countrycode = country.code  
join countrylanguage on city.countrycode=countrylanguage.countrycode;  





### length



### concat : 글자 합치기  

select concat('my','sql op', 'en source')  





### select locate('abc','ababababcab')  





### 글자 왼쪽부터, 오른쪽부터 뽑아내기

select 
left('mysql is an open source relational',5),  
right('mysql is an open source relational',7);  





### replace  

select replace('mysql','ms','my')  





### trim : 공백, 문자 없애는 함수  

select trim('      mysql     ');  





### leading은 앞에 샵이있으면 없애고, traing 은 뒤에  

select trim('    mysql  '),  
trim(leading '#' from '###mysql##'),  
trim(traing '#' from '###mysql##')  
 




### 3자리수로 끊기  

select format (123123123123123.123123123,3);  



### 내리기, 올리기 , 반올림  

select floor(10.95), ceil(10.95), round(10.95)  

select sqrt(4), pow(2,3), exp(3),log(3);  

