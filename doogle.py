# import cx_Oracle
# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.alexa.com/topsites/'
# recvd = requests.get(url)
# dom = BeautifulSoup(recvd.text, 'lxml')
# trs = dom.find_all(class_ = 'tr site-listing')
# sql = '''insert into ranking(rno, rank, sitename, info1, info2, info3, info4) values(s_ranking.nextval,{},'{}','{}','{}','{}','{}')'''
# conn = cx_Oracle.connect('doogle/enffl@localhost:1521/xe')
# cur = conn.cursor()
# for tr in trs:
#         tds = tr.find_all(class_ = 'td')
#         rank = tds[0].text
#         sitename = tds[1].text.strip()
#         info1 = tds[2].text.strip()
#         info2 = tds[3].text.strip()
#         info3 = tds[4].text.strip()
#         info4 = tds[5].text.strip()
#         cur.execute(sql.format(rank, sitename, info1, info2, info3, info4))
# conn.commit()
# conn.close()

# url = 'https://www.kurly.com/shop/goods/goods_list.php?category=907001'
# res = requests.get(url)
# dom = BeautifulSoup(res.text, 'lxml')
# lis = dom.find_all(class_='#goodsList ul.list > li')
# for li in lis:
#     print(li.text)
#     break