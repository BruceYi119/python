import os
import pymysql as my

con = my.connect(host='localhost',user='oneteam',password='enffl',db='oneteam',charset='utf8')
cur = con.cursor()
sql = '''insert into cancelled(yy,mm,cnt) values({},{},{})'''

with open(os.path.join('data','2007cancel.csv')) as f:
    for line in f:
        data = line.split(',')

        cur.execute(sql.format(data[0],data[1],data[2].strip()))

con.commit()
con.close()