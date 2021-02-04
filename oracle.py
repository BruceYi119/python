import cx_Oracle

con = cx_Oracle.connect("happy", "day", "localhost/xe")

cur = con.cursor()
cur.execute("select * from webtoon")
res = cur.fetchall()

for row in res:
    print(row)