import pymysql as my

# db연결
con = my.connect(host = 'localhost', user = 'root', password = '1234', db = 'pythondb', charset = 'utf8')

# 커서생성
# my.cursors.DictCursor dict로 가져오기
# 기본은 tuple
cur = con.cursor(my.cursors.DictCursor)

# 쿼리생성
sql = 'select * from member'

# 실행처리
cur.execute(sql)

for row in cur.fetchall():
    print(row)

name = input('이름=')
age = input('나이=')
email = input('이메일=')
birthyear = input('생일=')
sql = 'insert into member(name,age,email,birthyear) values(%s,%s,%s,%s)'
cur.execute(sql, (name,age,email,birthyear))

sql = 'select * from member'
cur.execute(sql)
for row in cur.fetchall():
    print(row)

con.commit()
# 자원해제
con.close()