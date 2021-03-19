import os
import requests
import numpy as np
from PIL import Image
import urllib.request
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# def search():
#     url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'
#     text = ''
#     for i in range(1,101):
#         r = requests.get(url.format(i))
#         dom = BeautifulSoup(r.text, 'lxml')
#         trs = dom.select('table.list_netizen > tbody > tr')
#         for tr in trs:
#             title = tr.select_one('td.title > a').text.replace(',','')
#             score = tr.select_one('td.title em').text
#             text += '{},{}\n'.format(title, score)
#
#     with open(os.path.join('data','movie.csv'), 'w', encoding='utf-8') as f:
#         f.write(text[:-1])

# search()

def cloud():
    o = Okt()
    text = ''
    with open(os.path.join('data', 'movie.csv'), encoding='utf-8') as f:
        text = f.read()

    data = text.split('\n')
    str = ''
    for d in data:
        s = d.split(',')
        str += '{} '.format(s[0])

    lines = text.split(' ')
    worddic = {}
    for line in lines:
        mal = o.pos(line, norm=True, stem=True)
        stopwords = ['있다','위해','하다','되다','안하다','최근','이번','기준']
        for m in mal:
            if len(m[0])>1 and m[1] == 'Noun' and m[0] not in stopwords:
                if not(m[0] in worddic):
                    worddic[m[0]] = 0
                worddic[m[0]] = worddic[m[0]] + 1

    dic = dict(sorted(worddic.items(), key=lambda x:x[1], reverse=True)[:100])
    img = Image.open(os.path.join('img','wine.png'))
    mask = np.array(img)
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 0:
                mask[i][j] = 255
    wc = WordCloud(max_font_size=100, mask=mask, background_color='white', font_path='C:\\Windows\\Fonts\\batang.ttc', max_words=99).generate_from_frequencies(dic)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

cloud()