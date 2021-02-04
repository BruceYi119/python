import os
import json
import datetime
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

# def test(a,b=0,c=0):
#     return a + b + c
#
# df = pd.DataFrame({ 'a': [1,2,3], 'b': [10,20,30]})
# print(df['a'].apply(test,b=1,c=2))
# print(df['b'].apply(test,b=10,c=9,axis=1))

# df = pd.DataFrame({'name': ['kim','park','lee','kim'],'grade': [1,2,3,2],'kor': [10,30,60,20], 'eng': [90,50,60,40], 'date': ['2020-12-12','2020-12-31','2021-01-01','2020-01-05']})
# print(df.groupby(['name','grade'])[['kor','eng']].sum())
# print(df.groupby(['name','grade'])[['kor','eng']].apply(lambda d: d + 1))

# def cf(d, a=2):
#     return d+11+a

# agg 메서드
# print(df.groupby('name')['kor'].min())
# print(df.groupby('name')['kor'].agg(['sum','min','mean','max','median','std']))
# print(df.groupby('name').agg({'kor': 'sum', 'eng': 'mean'}))
# print(df.groupby(['name','grade']).agg({'kor': ['sum','min','mean'], 'eng': lambda d: d * 5 }))
# print(df.groupby(['name','grade']).agg({'kor': lambda d: d - 1, 'eng': lambda d: d * 5 }))
# print(df.groupby(['name','grade']).agg({'kor': cf, 'eng': lambda d: d * 5 }))
# print(df.groupby(['name','grade']).agg({'kor': lambda d: cf(d, a=3), 'eng': lambda d: d * 5 }))

# 토-일 제외한 평일만추출
# print(pd.date_range(start='2020-12-07',end='2021-01-05', freq='B'))
# 월요일만 추출
# print(pd.date_range(start='2020-12-07',end='2021-01-05', freq='W-MON'))
# 일요일만 추출
# print(pd.date_range(start='2020-12-07',end='2021-01-05', freq='W-SUN'))
# 수/금요일만 추출
# print(pd.date_range(start='2020-12-07',end='2021-01-05', freq='W-WED'))

dtlist = list(pd.date_range(start='2015-01-02',end='2015-01-05'))
data = pd.read_csv(os.path.join('data','ebola.csv'))
data = data[data['Date'] >= '1/3/2015']
print(data)