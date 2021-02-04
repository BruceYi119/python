import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# tips = sb.load_dataset('tips')
# print(tips.groupby('day')['total_bill'].mean())

# 섞여진 10개의 고정된 데이터가져오기
# tips10 = tips.sample(10, random_state=42)

# g1 = tips10.groupby('sex')
# print(g1)
# 그룹객체 속성
# print(g1.groups)
# 그룹객체의 메서드 (특정 그룹만 추출)
# print(g1.get_group('Female'))

# g2 = tips10.groupby(['sex','time']).total_bill.mean()
# print(g2.values)
# print(type(g2))
# d2 = g2.reset_index()
# print(d2)
# print(type(d2))
# print(d2.sort_values(['time','total_bill']))

# data = pd.read_csv(os.path.join('data','accident.csv'))

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

# 막대 그래프
# d1 = data[data['사상자수'] >= 3]
# d1 = d1.groupby('요일')['사상자수'].sum()
# d1 = d1.reindex(['월','화','수','목','금','토','일'])
# d2 = d1.reset_index()
# # plt.plot(d1)
# plt.plot(d2['요일'],d2['사상자수'])
# plt.title('2012-2014 교통사고 요일별 사상자수 합')
# plt.xlabel('요일')
# plt.ylabel('사상자수')
# plt.show()

# 원 그래프
# data = pd.read_csv(os.path.join('data','accident.csv'))
# data = data[data['발생지시도'] == '경기']
# data = data.groupby('발생지시군구')
# data = data['사망자수'].sum()
# data = data.sort_values(ascending=False)
# data = data[range(0,5)]
# plt.plot(data.index, data.values, 'o')
# plt.show()
# plt.pie(data.values,labels=data.index,colors=['orange','blue','pink','brown','yellow'],autopct='%.2f%%')
# plt.title('2012-2014 경기도 교통사망사고 높은 지역 탑5')
# plt.show()

# data = pd.read_csv(os.path.join('data','movies.dat'),sep='::',names=[''])
# print(data)

c1 = pd.read_csv(os.path.join('data','concat_1.csv'))
c2 = pd.read_csv(os.path.join('data','concat_2.csv'))
c3 = pd.read_csv(os.path.join('data','concat_3.csv'))
data = pd.concat([c1,c2,c3],ignore_index=True,axis=1)
print(data)
################################################################################################################################################

# g2=g2.sort_values(ascending=False).head()
# print(g2)
# # plt.plot(g2.index,g2.values,'o')
# # plt.show()
# plt.pie(g2,labels=g2.index,
#         colors=['red','green','blue','yellow','purple'],
#         autopct='%.2f%%')
# # plt.pie(g2,labels=['화성시','평택시','용인시','수원시','고양시'])
# plt.title('2012-2014 경기도 교통사망사고 높은 지역')
# plt.show()
# movies=pd.read_csv('data/ml-1m/movies.dat',sep='::',
#                    names=['MovieID','Title','Genres'])
# print(movies)
# ratings=pd.read_csv('data/ml-1m/ratings.dat',sep='::',
#     names=['UserID','MovieID','Rating','Timestamp'])
# print(ratings)
# users=pd.read_csv('data/ml-1m/users.dat',sep='::',
#     names=['UserID','Gender','Age','Occupation','Zip-code'])
# print(users)
# c1=pd.read_csv('data/concat_1.csv')
# # print(c1)
# c2=pd.read_csv('data/concat_2.csv')
# # print(c2)
# c3=pd.read_csv('data/concat_3.csv')
# # print(c3)
# # 데이터의 연결
# # concat:한번에 2개이상의 데이터프레임을 연결
# # data=pd.concat([c1,c2,c3])
# # print(data)
# # print(data.loc[3])
# # data=pd.concat([c1,c2,c3],ignore_index=True)
# # print(data)
# # -------------------------
# print(c1)
# c2['e']='eee'
# print(c2)
# print(c3)
# # data=pd.concat([c1,c2,c3],ignore_index=True)
# # print(data)
# # 열방향 합치기
# data=pd.concat([c1,c2,c3],ignore_index=True,axis=1)
# print(data)
# print('\n\n\n\n\n\n\n\n\n')