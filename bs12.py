import os
import cx_Oracle
from bs4 import BeautifulSoup
import requests

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
r = requests.get(url)
dom = BeautifulSoup(r.content, 'lxml')
loc = dom.find_all('location')

# with open(os.path.join('data','weather.xml'), 'w', encoding='utf-8') as f:
#     f.write(r.text)

str = ''

for row in loc:
    province = row.find('province').text
    city = row.find('city').text
    data = row.find_all('data')

    for r in data:
        mode = r.find('mode').text
        tmef = r.find('tmef').text
        wf = r.find('wf').text
        tmn = r.find('tmn').text
        tmx = r.find('tmx').text
        rnst = r.find('rnst').text

        str += '{},{},{},{},{},{},{},{}\n'.format(province,city,mode,tmef,wf,tmn,tmx,rnst)

with open(os.path.join('data','weather.csv'), 'w', encoding = 'utf-8') as f:
    f.write(str[:-1])