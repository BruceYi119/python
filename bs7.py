import os
import re
import time
import requests
import json
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
r = requests.get(url)
json = json.loads(r.text)

def dataWrite():
    data = ''

    for row in json['list']:
        title = row['title']
        content = row['subContent']

        data += "{}::{}\n".format(title, content)

    with open(os.path.join('data','sports.csv'), 'w', encoding='utf-8') as f:
        f.write(data[0:-1])

if __name__ == '__main__':
    dataWrite()