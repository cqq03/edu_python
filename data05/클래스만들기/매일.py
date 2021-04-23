class Day:
    study = ''
    hours = None
    place = ''
    def __init__(self, study, hours, place):
        self.study = study
        self.hours = hours
        self.place = place
    def studying(self, study, hours):
        return study + '를 ' + str(hours) + '시간 하다'
    def where(self, study, place):
        return place + '에서 ' + study + '를 하다'
    def __str__(self):
        return self.study + ', ' + str(self.hours) + ', ' + self.place
if __name__ == '__main__':
    day1 = Day('파이썬공부', 10, '강남')
    print(day1)
    print(day1.studying('파이썬공부', 10))
    print(day1.where('파이썬공부', '강남'))