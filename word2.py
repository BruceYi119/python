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

# str = '백신이 내일부터 접종 시작한다고 합니다.'
# h = Hannanum()
o = Okt()

# print(str)
# print(h.pos(str))
# print(h.nouns(str))

# norm : 문장정규화, stem : 원형추출
# print(o.pos(str, norm=True, stem=True))
# print(o.nouns(str))

# client_id = "BQ1uoKa6ERSfHgNoDpx7"
# client_secret = "vu9DMk8ZJq"
# encText = urllib.parse.quote("둘리")
# url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # json 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     data = json.loads(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

# with open(os.path.join('data', 'dooly.csv'), 'a', encoding='utf-8') as f:
#     for d in data['items']:
#         str = d['description']
#     str = re.sub(r'(\<[a-z]+\>|\<\/[a-z]+\>|\‘|\’)', '', str)
#     str = re.sub(r'(\.\.\.|\,)', ' ', str)
#     f.write(str + '\n')

# with open(os.path.join('data', 'dooly.csv'), encoding='utf-8') as f:
#     text = f.read()

# lines = text.split('\n')
# for line in lines:
#     print(o.pos(line, norm=True, stem=True))
#     break

# sw = STOPWORDS
# sw.add('said')
# img = Image.open(os.path.join('img','clap.png'))
# mask = np.array(img)
# wc = WordCloud(max_font_size=100,mask=mask,background_color='white', stopwords=sw, font_path='C:\\Windows\\Fonts\\batang.ttc').generate(lines[0])
# plt.imshow(wc)
# plt.axis('off')
# plt.show()

# a = [3,1,2]
# print(sorted(a))
# print(sorted(a,reverse=True))
# b = {'one':100,'four':4,'three':33}
# print(sorted(b))   # ['four', 'one', 'three']
# for i in b:
#     print(i)
# for i in b.items():
#     print(i)
# print(sorted(b.items(), key=lambda x:x[1]))
# print(sorted(b.items(), key=lambda x:x[1], reverse=True))
# print(b.items())

with open(os.path.join('data', 'news.csv'),encoding='utf-8') as f:
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
img = Image.open(os.path.join('img','clap.png'))
mask = np.array(img)
wc = WordCloud(max_font_size=100, mask=mask, background_color='white', font_path='C:\\Windows\\Fonts\\batang.ttc', max_words=99).generate_from_frequencies(dic)
plt.imshow(wc)
plt.axis('off')
plt.show()