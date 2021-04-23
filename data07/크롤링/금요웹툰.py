import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekdayList.nhn?week=fri"
result = requests.get(url)
#print(result.content)
# result

content = BeautifulSoup(result.content, "html.parser")

# content

dt_list = content.findAll("dt")
# dt_list : ResultSet class의 객체, LIST의 상속!
# 인덱싱과 슬라이싱이 된다.

dd_list = content.findAll("dd", {"class": "desc"})
print(dd_list)
print('리스트의 개수2 >', len(dd_list)) #리스트의 개수
print(dd_list[0])
tag2 = dd_list[0]
print(type(tag2))
print(tag2.text)
print('----------------------------')

for item in dd_list:
    print(item)
print('----------------------')
for index in range(0, len(dd_list)):
    print(dd_list[index])

print('-------')
div_list = content.findAll("div", {"class": "rating_type"})
title_list = []
for tag in dt_list:
    print(tag.find('a').text)
    data = tag.find('a').text
    title_list.append(data)
print(len(title_list))
print(title_list[3:])
print('------------')
writer_list = []
for tag2 in dd_list:
    print(tag2.find('a').text)
    data = tag2.find('a').text
    writer_list.append(data)
print(len(writer_list))
print(writer_list[3:])
jumsu_list = []
for tag3 in div_list:
    print(tag3.find('strong').text)
    data = tag3.find('strong').text
    jumsu_list.append(data)
print(len(jumsu_list))
print(jumsu_list)

# writer_list = []
# for index in range(0, 145):
#     data = num_list[index].text
#     jumsu_list.append(data)
# print(len(jumsu_list))
# print(jumsu_list)
#
# title_list2 = tuple(title_list)
# print(title_list2)
#
# jumsu_list2 = tuple(jumsu_list)
# print(jumsu_list2)
import 크롤링.webtoon_crud as db
#  db.create(jumsu_list2)

total = list(zip(title_list[3:], writer_list[3:], jumsu_list)) #zip함수 꺼내오고 만들어주고 꺼내오고 만들어주고 하나하나 만들어주는 함수
print(total)
total2 = tuple(total)
print(total2)
db.create(total2)