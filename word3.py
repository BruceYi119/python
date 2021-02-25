# konlpy
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype

import os
import sys
import json
import re
import numpy as np
from PIL import Image
import urllib.request
from konlpy.tag import Okt
import matplotlib.pyplot as plt
# from konlpy.tag import Hannanum
from wordcloud import WordCloud, STOPWORDS

o = Okt()

with open(os.path.join('data', 'news2.csv'),encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')
worddic = {}                                        # {'바이러스':100,'인기':30,'백신':5,....}
for line in lines:
    mal = o.pos(line, norm=True, stem=True)         # [('지난해', 'Noun'), ('글로벌', 'Noun'), ('ESG', 'Alpha'),....,('ESG', 'Alpha')]
    stopwords = ['있다','위해','하다','되다','안하다','최근','이번','기준']
    for m in mal:                                   # m = ('지난해', 'Noun'),('ESG', 'Alpha')
        if len(m[0])>1 and m[1] == 'Noun' and m[0] not in stopwords:
            if not(m[0] in worddic):
                worddic[m[0]] = 0
            worddic[m[0]] = worddic[m[0]] + 1

dic = dict(sorted(worddic.items(), key=lambda x:x[1], reverse=True)[:100])
img = Image.open(os.path.join('img','apple.png'))
mask = np.array(img)
# 마스크 이미지 적용 안될때 이미지 처리
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] == 1:
            mask[i][j] = 255
wc = WordCloud(max_font_size=100, mask=mask, background_color='white', font_path='C:\\Windows\\Fonts\\batang.ttc', max_words=99).generate_from_frequencies(dic)
plt.imshow(wc)
plt.axis('off')
plt.show()