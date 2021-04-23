
def exam01(x, y):
    print('아이디가', x + '인', y + '님이 로그인되었습니다.')

def exam02(n1, n2):

    print('숫자1:', n1)
    print('숫자2:', n2)
    print('--------------')
    print('두 수의 합은', n1 + n2)
    print('두 수의 차은', n1 - n2)
    print('두 수의 곱은', n1 * n2)
    print('두 수의 나눗셈은', n1 / n2)
    print('나누고나서의 나머지', n1 % n2)

def exam03():
    x = input()
    y = input()
    print(x + '님의', '10년 후의 나이는', int(y) + 10, '세입니다.')
def exam04():
    x = int(input('엄마 용돈주세요: '))
    if x > 10000:
        print('엄마 너무 용돈이 많아요.')
    else:
        print('엄마 너무 용돈이 적어요.')

def exam05():
    x = int(input())
    if x % 2 == 1:
        print('입력한 값은 홀수')
    else:
        print('입력한 값은 짝수')
def exam06():
    x = input('실적을 입력하세요>> ')
    y = int(x)
    if y >= 1000:
        print('축하합니다. 실정을 달성하셨습니다.!')
        print('당신의 이번달 보너스는', int(y * 0.2), '만원입니다.')
def exam07():
    x = input('미사일 이름은: ')
    y = input('미사일 시작값은: ')
    z = input('미사일 움직이는 값은: ')
    print('--------------------------------')
    print(x, '미사일이', int(y) + float(z),'로 이동되었습니다.')
def exam08():
    x = input('받은 돈: ')
    y = input('상품의 총액: ')
    z = int(y)/10
    print('받은 돈:', x)
    print('상품의 총액:', y)

    print('부가세:', int(z))
    print('잔돈:', int(x) - int(y))

def exam09():
    for _ in range(1000):
        print('*', end='')