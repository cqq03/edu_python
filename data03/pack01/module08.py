#for문을 사용해주세요
#range: 범위를 주고 범위 안에서 카운트하면서 하는 것
# 1. range(20) print!
for x1 in range(20):
    print(x1)
# 2. 1부터 100까지 print!
for x2 in range(1, 101, 1):
    print(x2)
# 3. 0부터 200까지  print!
for x3 in range(0, 201, 1):
    print(x3)
#4. 1부터 100까지 중 2씩 점프해서 print
for x4 in range(1, 101, 2):
    print(x4)
#5. 100부터 500까지 5씩 점프해서 print
for x5 in range(100, 501, 5):
    print(x5)
#6. 100부터 500까지 중 10씩 점프해서 모두 더해서 프린트
sum1 = 0
for x6 in range(100, 501, 10):
    sum1 = sum1 + x6
print(sum1)
#7. 3부터 200까지 중 8씩 점프한 값을 모두 곱해서 print!
sum2 = 1
for x7 in range(3, 201, 8):
    sum2 = sum2 * x7
print(sum2)

#------

#8. food = ['감자', '고구마', '양파']를 다음과 같이 print!
#8-1
food = ['감자', '고구마', '양파']
for x8 in food:
    print(x8 + '짱!')
#8-2
for x9 in food:
    print(x9 + '짱! ', end='')
print()

#9. food2 = "감자 고구마 양파 스프 국수 라면"을 다음과 같이 프린트
food2 = ['감자', '고구마', '양파', '스프', '국수', '라면']
for x10 in food2:
    if x10 != '양파' and x10 != '국수':
        print(x10 + '맛있어! ', end='')