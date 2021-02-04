import os
import json
import datetime
import seaborn as sb
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
print(data)

################################################################################################################################################
# data=pd.read_excel('data\\시도별 전출입 인구수.xlsx')
# # print(data)
# data=data.fillna(method='ffill')
# # print(data)
# df=data[(data['전출지별']=='서울특별시') &
#         (data['전입지별']!='서울특별시')]
# # print(df)
# df=df.drop('전출지별',axis=1)  #열삭제
# # print(df)
# df=df.set_index('전입지별')
# print(df)
# # 선그래프
# # plt.plot([30,20,5,10],'o')
# plt.plot([1,2,3,4],[30,20,5,10],'o')
# plt.xticks([1,2,3,4])
# # plt.yticks([0,20,40,60])
# plt.yticks(list(range(0,61,20)))
# plt.show()
# print(df.loc['부산광역시'])   #시리즈
# plt.style.use('bmh')
# plt.plot(df.loc['부산광역시'])
# plt.plot(df.loc['제주특별자치도'])
# plt.xticks(rotation='90',size=7)
# plt.xlabel('년도')
# plt.ylabel('건수')
# plt.title('년도별 서울에서 타지방으로 이동량')
# plt.legend(['부산','제주'])
# plt.show()
# ----------------
# print('스타일',plt.style.available)
# ---------------------
# car=pd.read_csv('data\\mpg.csv',header=None)
# # 행인덱스 car.index
# # 열인덱스 car.columns
# # print(car)
# car.columns=['mpg','cyn','disp','horsepower','weight',
#              'acc','modelyear','country','name']
# # print(car)
# # car.info()
# # country를 이용하여 country1 컬럼생성
# #      1->미국,2->유럽,3->일본
# def getCountry1(x):
#     if x==1:
#         return '미국'
#     elif x==2:
#         return '유럽'
#     else:
#         return '일본'
# car['country1']=car['country'].apply(getCountry1)
# print(car)
# 연비의 상자그림, 히스토그램
# plt.boxplot(car['mpg'])
# plt.show()
# plt.hist(car['mpg'])
# plt.show()
# 제조국별 연비의 상자그림과 히스토그램
# print(car[car['country1']=='미국']['mpg'])
# plt.boxplot([car[car['country1']=='미국']['mpg'],
#             car[car['country1']=='유럽']['mpg'],
#              car[car['country1']=='일본']['mpg']],
#             labels=['미국','유럽','일본'])
# plt.show()
# 미국산 자동차 연비의 히스토그램
# plt.hist(car[car['country1']=='미국']['mpg'])
# plt.show()
# 우리시장의 제조국별 자동자 수
# s1=car.groupby('country1').count()  #모든열의 데이터갯수세기
# s1=car.groupby('country1').size() #행의 수 세기
# print(s1)   #시리즈
# plt.pie(s1,labels=s1.index,autopct='%.1f%%')
# plt.show()
# 연비와 무게 사이의 관계
# plt.scatter(car['mpg'],car['weight'])
# plt.show()
# print('\n\n\n\n\n')
# # 과제
# # gap.tsv 를 읽어 아프리카 대륙의 나라별 기대수명을 선그래프로 그리세요
# 1)아프리카 대륙의 데이터만 필터링 한다
# 2)1번의 데이터를 활용하여 그래프를
