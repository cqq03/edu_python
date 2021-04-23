from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my


def free():
    print('쉬다.!')


class WomanDay(Person, my.Day):
    # 파이썬: 클래스간 다중 상속이 가능하다.
    # 자바: 클래스간 단일상속만 가능하다.
    def __init__(self, study, hours, place):
        my.day.__init__(self, study, hours, place)

    def __str__(self):
        return self.study + ', ' + self.hours + ', ' + self.place


if __name__ == '__main__':
    woman_day1 = WomanDay('진짜 놀기', 10, '신촌')
    free()
    woman_day1.eat()
