import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url)
#print(result.content)
# result

content = BeautifulSoup(result.content, "html.parser")

# content

dt_list = content.findAll("dt", {"class": "tit"})
# dt_list : ResultSet class의 객체, LIST의 상속!
# 인덱싱과 슬라이싱이 된다.
print(type(dt_list)) #ResultSet클래스의 객체
print(dt_list) #전체 목록 프린트
print('리스트의 개수 >', len(dt_list)) #리스트의 개수
print(dt_list[0])
tag = dt_list[0].find("a")
print(tag)
print(type(tag))
print(tag.text)

num_list = content.findAll("span", {"class": "num"})
print(num_list)
print('리스트의 개수2 >', len(num_list)) #리스트의 개수
print(num_list[0])
tag2 = num_list[0]
print(type(tag2))
print(tag2.text)
print('----------------------------')

for item in num_list:
    print(item)
print('----------------------')
for index in range(0, len(num_list)):
    print(num_list[index])
print('==============================================')
for tag in num_list:
    print(tag.text)
for index in range(0, len(num_list), 2):
    print(index, ':', num_list[index].text)#arraylist와 같음

print('-------')
title_list = []
for tag in dt_list:
    print(tag.find('a').text)
    data = tag.find('a').text
    title_list.append((data))
print(len(title_list))
print(title_list)
print('------------')

jumsu_list = []
for index in range(0, 145, 2):
    data = num_list[index].text
    jumsu_list.append(data)
print(len(jumsu_list))
print(jumsu_list)

title_list2 = tuple(title_list)
print(title_list2)

jumsu_list2 = tuple(jumsu_list)
print(jumsu_list2)
# #
import 크롤링.movie_crud as db
#  db.create(jumsu_list2)
jumsu_list3 = list(jumsu_list2)
total = list(zip(title_list2, jumsu_list2)) #zip함수 꺼내오고 만들어주고 꺼내오고 만들어주고 하나하나 만들어주는 함수
print(total)
total2 = tuple(total)
print(total2)
db.create(total2)
# dt_list[0].find("a").text
#
# title = []
# for dt in dt_list:
#     title.append(dt.find("a").text)
#
# # title
#
# len(dt_list)
#
# score_list = content.select('dl.info_star dd div.star_t1 a span.num')
# # score_list
#
# len(score_list)
#
# scores = []
# for score in score_list:
#     scores.append(float(score.text))
#
# # scores
#
#
# df = pd.DataFrame({"영화이름": title, "영화평점": scores})
# # df
#
# print(df)  # dataFrame
# print(df[10:20])  # 10~19
# result = df.describe()  # 자세한 설명
# print(result)
# print(df.head(3))  # 앞에서 3개
# print(df.info())  # 데이터 타입
# print(df.index)  # 인덱스
# print('영화이름')
# print('---------------------')
# print(df['영화이름'])
# print('---------------------')
# print(df['영화평점'])
# print(df.sort_values(by='영화평점', ascending=False))