import db연결.mysql연결테스트 as db

id = input('아이디를 입력하세요.')
pw = input('패스워드를 입력하세요.')
name = input('이름를 입력하세요.')
tel = input('전화번호를 입력하세요.')
db.create(id, pw, name, tel)