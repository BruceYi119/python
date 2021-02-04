import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

# 1880-2010
tmp = []
for year in range(1880, 2011):
    filename = 'yob' + str(year) + '.txt'
    d = pd.read_csv(os.path.join('data','baby',filename), names=['name','sex','births'])
    d['year'] = year
    tmp.append(d)

# data = pd.concat(tmp)
# 기존 index를 무시하고 모두 합치기
data = pd.concat(tmp,ignore_index=True)
# data.sort_values(by='컬럼명')

# 년도와 성별에 따른 출생아수
data = data.groupby(['year','sex'])['births'].sum()
print(data)