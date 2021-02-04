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
data = data[(data['전출지별'] == '서울특별시') & (data['전입지별'] != '서울특별시')]
data = data.drop('전출지별', axis=1)
data = data.rename(columns={ '전입지별': '전입지' })
data = data.set_index('전입지')
data = data.loc[['경기도','부산광역시','광주광역시','제주특별자치도'],:]
data = data.transpose()  #행열전환
data['광주광역시'] = pd.to_numeric(data['광주광역시'],errors='coerce')
data['광주광역시'] = data['광주광역시'].fillna(0)

fig = plt.figure(figsize=(30, 5))
g1 = fig.add_subplot(2,2,1)
g2 = fig.add_subplot(2,2,2)
g3 = fig.add_subplot(2,2,3)
g4 = fig.add_subplot(2,2,4)
g1.plot(data['경기도'])
g2.plot(data['부산광역시'])
g3.plot(data['광주광역시'])
g4.plot(data['제주특별자치도'])
g1.set_title('서울->경기')
g2.set_title('서울->부산')
g3.set_title('서울->광주')
g4.set_title('서울->제주')
fig.suptitle('서울에서 경기, 부산, 광주, 제주로 이사한 데이터를 한화면에 선 그래프로 각각 그리세요')
fig.tight_layout()
plt.legend(loc='upper center')
plt.show()