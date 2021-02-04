# import bs4
from bs4 import BeautifulSoup
import os
import requests
import re
import time

# os.path.join()
# dataPath = os.path.join('data/test.html')
#
# with open(dataPath, 'r', encoding='utf-8') as f:
#     html = f.read()
#     dom = BeautifulSoup(html, 'lxml')

# print(html)
# print(dom.find_all(class_ = 'ppp3'))
# print(dom.find_all(id = 'pid3'))
# print(dataPath)
#
# print(os.cpu_count())
# print(os.path)
# print(os.getpid())
#
# print(dom)
# print(dom.find('a')['href'])
# print(dom.find('img')['src']))

# www.naver.com/robots.txt
# url = 'https://comic.naver.com/webtoon/list.nhn?titleId=730656&weekday=tue'
# r = requests.get(url)
# dom = BeautifulSoup(r.text, 'lxml')
# imgs = dom.find_all('img')
#
# i = 0;
# for img in imgs:
#     print(img['src'])
#     try:
#         c = requests.get(img['src'])
#         p = re.compile('(png|jpg|gif)$')
#         m = p.findall(img['src'])
#         fileName = 'img\\' + str(i) + '.' + m[0]
#         with open(fileName, 'wb') as f:
#             f.write(c.content)
#         i += 1
#     except:
#         print('이미지 정보 없음')

# a = 'A'
# b = 'B'
# c = 'C'
# d = '{}/{}/{}'.format(a,b,c)
# print(d)

for page in range(1, 9):
    url = 'https://comic.naver.com/webtoon/list.nhn?titleId=730656&weekday=tue&page={}'.format(page)
    r = requests.get(url)
    dom = BeautifulSoup(r.text, 'lxml')
    trs = dom.find('table', class_ = 'viewList').find_all('tr');

    for tr in trs:
        time.sleep(1)

        try:
            img = tr.find('td').find('img')
            title = img['title']
            src = img['src']
            c = requests.get(src)
            p = re.compile('(png|jpg|gif)')
            m = p.findall(src)
            file = 'img\\' + title + '.' + m[0]

            with open(file, 'wb') as f:
                f.write(c.content)
        except:
            print('이미지 정보가 없습니다')