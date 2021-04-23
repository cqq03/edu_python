names = ['홍길동', '김길동', '박길동']
ages = [100, 200, 300]

total= list(zip(names, ages))
print(len(total))
print(total)
print(type(total))
total2 = tuple(total)
print(total2)