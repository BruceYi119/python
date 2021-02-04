import os
import json
import pandas as pd
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = json.load(open(os.path.join('data','python.json'), encoding='utf-8'))
data = data['items']
data = pd.DataFrame(data, columns=['title','publisher','price','isbn'])
print('1)네이버개발자 센터에서 \'파이썬\'책을 100검색하여 책제목,출판사, 가격,isbn열을 데이터프레임 df로 생성하세요')
print(data)

print('2)출판사별 가격의 평균을 출력하세요')
data['price'] = data[['price']].apply(lambda d: int(d['price']), axis=1)
print(data.groupby('publisher').price.mean())