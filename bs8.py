import os
import re
import time
import requests
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

url = 'https://finance.daum.net/api/search/ranks?limit=10'
ua = UserAgent()
headers = {'user-agent': ua.ie, 'referer': 'https://finance.daum.net/'}
r = requests.get(url, headers=headers)
json = json.loads(r.text)

def dataWrite():
    data = ''

    for row in json['data']:
        rank = row['rank']
        name = row['name']
        tradePrice = row['tradePrice']

        data += "{},{},{}\n".format(rank,name,tradePrice)

    with open(os.path.join('data','stock.csv'), 'w', encoding='utf-8') as f:
        f.write(data[:-1])

if __name__ == '__main__':
    dataWrite()