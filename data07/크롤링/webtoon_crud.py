import pymysql #alt+Enter
#DAO역할 모듈: CRUD(DML)

#정형데이터 => mysql, oracle, sqlite3(관계형 데이터베이스 관리 시스템, RDBMS)
def create(datas):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)
    # sql = 'insert into movie2(jumsu) values (%s)'
    #sql = 'insert into movie2(title) values (%s)'
    sql = 'insert into webtoon(title, writer, jumsu) values (%s, %s, %s)'
    result = cur.executemany(sql, datas)
    print('처리결과', result, '갠')

    con.commit()
    con.close()
