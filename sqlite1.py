import sqlite3

# DB연결
con = sqlite3.connect("D:\sqlite\pythondb")
# 커서 생성
cur = con.cursor()
# 쿼리생성
sql = "select * from member"
# 쿼리실행
cur.execute(sql)

# sql = "insert into member values (4, '고길동')";
# cur.execute(sql)

def select(sql):
    cur.execute(sql)

    for row in cur.fetchall():
        print(row[0],":",row[1])

sql = "select * from member"
select(sql)

mno = input('번호=')
id = input('아이디=')
name = input('이름=')
sql = "insert into member(mno, id, name) values ({}, '{}', '{}')".format(mno, id, name)
cur.execute(sql)
sql = "delete from member"
cur.execute(sql)
con.commit()

# 자원해제
con.close()