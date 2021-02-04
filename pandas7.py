import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

# xlrd (pip install xlrd==1.1) 의존모듈 설치
ebola = pd.read_csv(os.path.join('data','ebola.csv'))
# print(ebola)
# ebola.info()
# print(ebola.shape)  #(122,18)
# print('값의 갯수\n',ebola.count())
# print('누락값의 갯수\n',ebola.shape[0]-ebola.count())
# e1=ebola.iloc[:10,:5]
# print(e1)
# 누락값 처리fillna()
# print('지정된 값으로 변경\n',e1.fillna(0))
# print('누락값 전의 값으로 변경\n',e1.fillna(method='ffill'))
# print('누락값 후의 값으로 변경\n',e1.fillna(method='bfill'))
# print('누락값 양쪽에 있는 값의 평균\n',e1.interpolate())
# print('누락값이 포함된 행 삭제\n',e1.dropna())
# 누락값이 포함된 연산
# e1['tot']=e1['Cases_Guinea']+e1['Cases_Liberia']+e1['Cases_SierraLeone']
# print(e1)
# e1['tot']=e1['Cases_Guinea'].fillna(0)+e1['Cases_Liberia'].fillna(0)+\
#           e1['Cases_SierraLeone'].fillna(0)
# print(e1)
# # print(e1.Cases_Guinea.sum())
# print(e1['Cases_Guinea'].sum())
# print(e1['Cases_Guinea'].sum(skipna=False))  #nan
# print(e1.Cases_Liberia.mean())
# 피벗테이블
# data=pd.DataFrame({키1:[],키2:[],키3:[]})
data = pd.DataFrame({
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천" ],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010" ],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 2632035],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
})

# pivot(행인덱스로 사용할 열,열인덱스로 사용할 열,데이터로 사용할열)
# pivot_table(데이터로 사용할열,행인덱스로 사용할 열,열인덱스로 사용할 열)
# p1=data.pivot('도시','연도','인구')
# p1=data.pivot_table(index='도시',columns='연도',values='인구')
# print(p1)
# print(type(p1))
# print(p1.index)
# print(p1.columns)
# p2=data.pivot_table(index=['도시','연도'],values='인구')
# print(p2)
# data = pd.read_excel(os.path.join('data','판매현황.xlsx'))
# print(data)
# data = pd.pivot_table(data2,index='분류',values='판매수량')
# data = pd.pivot_table(data,index='분류',values='판매수량',aggfunc=sum)
# print(data)
# data = pd.read_csv(os.path.join('data','accident.csv'))
# data = pd.pivot_table(data,index='분류',columns='판매량',values='사망자수',aggfunc=sum)
# data.reindex(['월','화','수','목','금','토','일'])
# print(data)

# data = pd.read_csv(os.path.join('data','movie_rating_user'))


######################################

# movies=pd.read_csv('data/ml-1m/movies.dat',sep='::',
#                    names=['MovieID','Title','Genres'])
# print(movies)
# ratings=pd.read_csv('data/ml-1m/ratings.dat',sep='::',
#     names=['UserID','MovieID','Rating','Timestamp'])
# print(ratings)
# users=pd.read_csv('data/ml-1m/users.dat',sep='::',
#     names=['UserID','Gender','Age','Occupation','Zip-code'])
# print(users)
# mr=pd.merge(movies,ratings,on='MovieID')
# print(mr)
# print(mr.columns)
# data=pd.merge(mr,users,on='UserID')
# print(data)
# # data.to_csv('data\movie2.csv',index=False,header=False)
# data.to_csv('data\movie2.csv',index=False)
# data=pd.read_csv('data\movie2.csv')
# print(data)
# print(data.columns)
# # 영화제목별 평점 건수
# titlecnt=data.groupby('Title')['Rating'].size()
# titlecnt=data.groupby('Title')['Rating'].count()
# print(titlecnt)   #시리즈
# # 평점정보가 200건 이상있는 영화
# r200=titlecnt[titlecnt>=200]

# # print(r200.index)  #평점정보가 200건 이상있는 영화제목
# data=data.set_index('Title')
# # print(data)
# data200=data.loc[r200.index]
# print(data200)
# data200=data200.reset_index()
# print(data200)
# ---------------------------------
# # 영화별 평균평점
# print(data200.groupby('Title').Rating.mean())
# # 성별에 따른 평균평점
# # print(data200.groupby(['Title','Gender']).Rating.mean())
# # 여성에서 높은 평점을 받은 영화 5
# s1=data200.groupby(['Title','Gender']).Rating.mean()
# d1=s1.reset_index()
# print(d1)
# d1=d1[d1['Gender']=='F']
# print(d1)
# print(d1.sort_values(by='Rating',ascending=False).head())
# -성별에 따른 영화평점----------------------
# p1=pd.pivot_table(data200,index='Title',columns='Gender',
#                   values='Rating')
# print(p1)
# # 남자들이 좋아하는 영화 10개
# print(p1.sort_values(by='M',ascending=False).head(10))
# # 남녀간에 호불호가 갈리는 영화 10개
# p1['diff']=(p1['F']-p1['M']).abs()
# print(p1)
# print(p1.sort_values(by='diff',ascending=False).head(10))
# 호불호가 갈리는 영화 10개
# g2=data200.groupby('Title')['Rating'].std()
# print('영화별 평점의 표준편차\n',g2)
# print(g2.sort_values(ascending=False).head(10))

# print('-'*30)
# import seaborn as sns
# tips=sns.load_dataset('tips')
# print(tips)
# # 요일별 식사건수
# g1=tips.groupby('day').size()
# print(g1)
# # 요일별 식사건수가 50건 이상인 데이터만 가지고 분석하고 싶음
# g2=g1[g1>=50]
# print(g2)   #시리즈
# print(g2.index)   #['Thur', 'Sat', 'Sun']
# print(g2.values)
# tips=tips.set_index('day')
# print(tips)
# print(tips.loc[g2.index])