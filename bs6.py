import os
import re
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn'
r = requests.get(url)
dom = BeautifulSoup(r.text, 'lxml')
print(dom.title)