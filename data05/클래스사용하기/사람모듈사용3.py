from 클래스만들기.사람모듈 import *


class Student(Person):
    grade = 0
    studyHours = 0

    def study(self, name, age, grade, studyHours):
        return self.name + ' ' + str(self.age) + ' ' + str(self.grade) + ' ' + str(self.studyHours)

    def __str__(self):
        return self.name + ', ' + str(self.age) + ', ' + str(self.grade) + ', ' + str(self.studyHours)


class Worker(Person):
    rank = None

    def work(self, name, age, rank):
        return str(self.age) + '살인 ' + name + '의 직위는 ' + rank + '입니다.'

    def __str__(self):
        return self.name + ', ' + str(self.age) + ', ' + self.rank


if __name__ == '__main__':
    s1 = Student()
    s1.name = '홍길동'
    s1.age = 100
    s1.grade = 1
    s1.studyHours = 15
    print(s1)
    print(s1.study('홍길동', 100, 1, 15))
    w1 = Worker()
    w1.name = '김길동'
    w1.age = 200
    w1.rank = '과장'
    print(w1)
    print(w1.work('김길동', 200, '과장'))
