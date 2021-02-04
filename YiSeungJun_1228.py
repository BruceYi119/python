import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

tmp = []

for year in range(1880,2011):
    filename = 'yob{}.txt'.format(year)
    data = pd.read_csv(os.path.join('data', 'baby', filename), names=['name','sex','births']);
    data['year'] = year
    tmp.append(data)

data = pd.concat(tmp, ignore_index=True)

print('1. 년도, 성별에 따른 출생아수 를 피벗')
data1 = pd.pivot_table(data,index='year',columns='sex',values='births',aggfunc=sum)
print(data1)

# plt.plot(data1['F'], label='여자')
# plt.plot(data1['M'], label='남자')
# plt.title('2. 1의 결과를 그래프로')
# plt.xlabel('년도')
# plt.ylabel('출생아수')
# plt.legend()
# plt.show()

print('3. 연도와 이름에 대한 전체 출생수를 피벗')
data = data[['year','name','births']]
data2 = pd.pivot_table(data, index='year',columns='name',values='births',aggfunc=sum)
data2 = data2.fillna(0)
print(data2.columns)