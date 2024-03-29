#기본 라이브러리(표준 라이브러라)
import math
import random
print(math.sqrt(9.0))
print(random.randint(1, 100))

# 연산자
# 산술, 대입, 비교, 논리
# 산술연산자
x = 100
y = 333
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) #나머지
print(x // y) #소수점 자르기, 정수부분만 추출!
# 대입연산자
# 파이썬에서는 변수의 생성과 타입이
#값을 대입할 때 결정된다.
# auto-typing

#비교연산자 => 비교의 결과가 논리형, 반복문, 조건문의 실행과 관련 됨
print(x == y)
print(x != y)

a = 10
#+=, -=, *=, /=
a *= 10 #a = a * 10
print(a)

#논리연산자:and(&&), or, not
id = 'root'
pw = '1234'
print(id == 'root' and pw == '1234')
print(id == 'root' or pw == '1232')

#멤버쉽 연산자: in(~안에)
member = ['홍길동','김길동','송길동']
print('정길동' in member)
print('홍길동' not in member)