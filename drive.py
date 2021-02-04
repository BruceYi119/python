import os
import pymysql as my

con = my.connect(host='localhost',user='root',password='enffl',db='mariaDB',charset='utf8')
cur = con.cursor()
sql = '''insert into drive(week,cnt) values('{}',{})'''

with open(os.path.join('data','2007.csv')) as f:
    for line in f:
        data = line.split(',')

        cur.execute(sql.format(data[0],data[1].strip()))

con.commit()
con.close()