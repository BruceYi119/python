import os
import json
import datetime
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_excel(os.path.join('data','시도별 전출입 인구수.xlsx'))
data = data.fillna(method='ffill')
# print(data.shape)
data = data[(data['전출지별'] == '서울특별시') & (data['전입지별'] != '서울특별시')]
# print(data.shape)
data = data.drop('전출지별', axis=1)
data = data.rename(columns={ '전입지별': '전입지' })
data = data.set_index('전입지')
data1 = data.loc['경기도']

# print('스타일 종류',plt.style.available)
# print('matplotlib에서 사용할수 있는 색의 종류')
# import matplotlib
# temp={}
# for n,h in matplotlib.colors.cnames.items():
#     temp[n]=h
# print(temp)

# 선그래프
# plt.plot(data)

# 점그래프
# plt.plot(data, 'o')

# plt.style.use('ggplot')
# plt.figure(figsize=(15,5))
# plt.plot(data, marker='o', markersize=10, markerfacecolor='green', color='bisque', linewidth=2)
# plt.title('서울->경기 이동',size=20)
# plt.xlabel('년도')
# plt.xticks(size=7,rotation=70)
# plt.ylabel('이동수')
# plt.legend(['서울->경기'],fontsize=7)
# plt.annotate('인구이동 증가',xy=(10,450000),fontsize=15,ha='center',rotation=30)
# plt.annotate('',xy=(19,550000),xytext=(4,300000),arrowprops=dict(arrowstyle='->',color='#FFE4C4',lw=5))
# plt.annotate('인구이동 감소',xy=(40,500000),fontsize=15,ha='center',rotation=-10)
# plt.annotate('',xy=(47,450000),xytext=(30,550000),arrowprops=dict(arrowstyle='->',color='#DEB887',lw=5))
# plt.show()

data2 = data.loc[['부산광역시','광주광역시','제주특별자치도'],:]
# print(data)
data2 = data.transpose()  #행열전환
# print(data)
data2['광주광역시'] = pd.to_numeric(data2['광주광역시'],errors='coerce')
# print(data)
data2['광주광역시'] = data2['광주광역시'].fillna(0)
# print(d2)
plt.style.use('ggplot')
plt.figure(figsize=(15,5))
plt.plot(data1)
plt.plot(data2['부산광역시'])
plt.plot(data2['광주광역시'])
plt.plot(data2['제주특별자치도'])
plt.title('서울->타지역 이동',size=20)
plt.xlabel('연도')
plt.ylabel('이동수')
plt.xticks(size=7,rotation=70)
plt.legend(['서울->경기','서울->부산','서울->광주','서울->제주'],fontsize=7)
plt.show()