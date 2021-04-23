#문제1
num1 = int(input('숫자1: '))
num2 = int(input('숫자2: '))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
#문제2
str1 = input('입력1: ')
int1 = input('입력2: ')
print(str1 + '은', int1 + '세입니다.')
if int(int1) > 100:
    print('나이가 많으시군요!')
else:
    print('아직 어리시군요!')
#문제3 변수에 대입
hobby = '달리기'
time = 10
print(hobby + '를', str(time) + '시간 했습니다.')
if hobby == '달리기' and time >= 10:
    print('오늘', hobby + '는 충분')
elif hobby == '달리기' or time <= 10:
    print('어떤 운동이든 시작하세요!!')