import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

# data1 = pd.read_csv(os.path.join('data','survey_person.csv'))
# data2 = pd.read_csv(os.path.join('data','survey_survey.csv'))
# data3 = pd.read_csv(os.path.join('data','survey_site.csv'))
# data4 = pd.read_csv(os.path.join('data','survey_visited.csv'))

# merge 두개의 데이터를 기준에 의해 연결
# data1 = pd.read_csv(os.path.join('data','survey_person.csv'),names=['person','personal','family'])
# data2 = pd.read_csv(os.path.join('data','survey_survey.csv'))
# data = pd.merge(data1,data2,on='person')
# print(data)

# data = pd.merge(data1,data2,left_on='ident',right_on='person')
# print(data1,'\n',data2,'\n',data)
# data = pd.merge(data,data4,left_on='taken',right_on='ident')
# print(data)

# data1 = pd.read_csv(os.path.join('data','movies.dat'),sep='::',names=['MovieID','Title','Genres'])
# data2 = pd.read_csv(os.path.join('data','ratings.dat'),sep='::',names=['UserID','MovieID','Rating','Timestamp'])
# data3 = pd.read_csv(os.path.join('data','users.dat'),sep='::',names=['UserID','Gender','Age','Occupation','Zip-code'])

# data = pd.merge(data1,data2,on='MovieID')
# data = pd.merge(data,data3,on='UserID')
# data = data.sort_values(by='MovieID')

# csv로 저장
# data.to_csv(os.path.join('data','movie_rating_user.csv'),index=False,header=False)
# data.to_csv(os.path.join('data','movie_rating_user.csv'),index=False)

# 영화 제목별 평점 건수
# data = pd.read_csv(os.path.join('data','movie_rating_user.csv'))
# data = data.groupby('Title').Rating.size()

# 평점 정보가 200건 이상있는 영화
# data = pd.read_csv(os.path.join('data','movie_rating_user.csv'))
# r200 = data.groupby('Title').Rating.size()
# r200 = r200[r200 >= 200]
# data = data.set_index('Title')
# data = data.loc[r200.index]
# data = data.reset_index()

# 영화별 평균 평점
# data1 = data.groupby('Title').Rating.mean()
# print(data)

# 성별에 따른 평균평점
# data2 = data.groupby(['Title','Gender']).Rating.mean()
# print(data)

# 여성에게서 높은 평점을 받은 영화 5
# data3 = data[data['Gender']]
# data3 = data[data['Gender'] == 'F']
# data3 = data3.sort_values(by='Rating',ascending=False).head()
# print(data3)

# 누락 값의 갯수
# data = sb.load_dataset('titanic')
# print(data.count())
# print('*' * 30)
# print(data.shape)
# print('*' * 30)
# print(data.shape[0] - data.count())
# print(data)

# 행의 갯수 (행, 열)
# print(data.shape)

# 브로드캐스킹 시리즈/데이터프레임의 데이터를 한꺼번에 연산
# print(data.shape[0] - data.count())