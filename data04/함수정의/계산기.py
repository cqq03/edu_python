def add(x, y):
    return x + y
def minus(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

#print(add(1000, 2000))#자기가 만든 것도 사용 가능 함수정의 위에 쓰면 안 됨.하나만 돌려서 테스트할 떄/
# 테스트하고 안 닫으면 사용할 때도 실행됨
if __name__ == '__main__': #이 상황에서는 다른 곳에서 메인은 실행 x
    print(add(1000, 2000))