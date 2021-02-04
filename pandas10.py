import os
import json
import datetime
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

# data = { 'k1': ['a','b','b','c','c','d'], 'k2': ['v','w','w','x','y','d'], 'data': [1,2,3,4,5,'d'] }
# df = pd.DataFrame(data)

# 중복데이터 확인
# print(df.duplicated('k1'))
# print(df.duplicated(['k1','k2']))

# 중복데이터 제거
# print(df.drop_duplicates('k1'))
# 뒤에데이터를 살림
# print(df.drop_duplicates('k1',keep='last'))
# 완벽하게 동일한것만 삭제
# print(df.drop_duplicates())

# food = json.load(open(os.path.join('data','food.json')))
# print(food)
# print(len(food))
# print()
# print(food[0].keys())
# print(food[0]['nutrients'])

# df = pd.DataFrame(food, columns=['id','group','description'])
# print(df)

# tmp = []
# for d in food:
#     nut = pd.DataFrame(d['nutrients'])
#     nut['id'] = d['id']
#     tmp.append(nut)

# data = pd.concat(tmp, ignore_index=True)
# data = data.drop_duplicates()
# 컬럼이름변경 전체수정
# df.columns = ['foodid','foodgroup','foodname']
# 일부 변경
# df = df.rename(columns={ 'description': 'foodname', 'group': 'foodgroup' })
# df = df.merge(data, on='id')
# data.info()
# print(df.groupby(['foodgroup','group']).value.mean())

data = pd.read_csv(os.path.join('data','bank.csv'), parse_dates = ['Closing Date','Updated Date'])
data['year'] = data['Closing Date'].dt.year
data['quarter'] = data['Closing Date'].dt.quarter
s1 = data.groupby(['year','quarter']).size()
d2 = s1.reset_index()
d2['new'] = d2['year'].astype(str) + '-' + d2['quarter'].astype(str)
plt.plot(d2['new'], d2[0])
plt.title('년도별 분기별 파산한 은행수')
plt.show()