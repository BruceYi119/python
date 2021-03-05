# ---분석용데이터구축
# import pandas as pd
# # 1)
# data=pd.read_csv('data\\alcol.csv')
# data=data.set_index('State')
# # print(data.head())
# # 2)
# # data_wine=pd.pivot_table(data, index='Year',columns='State',
# #                          values='Wine',aggfunc=sum)
# # print(data_wine)
# # # 3)
# data2009=data[data['Year']==2009]
# # print(data2009.shape)  #(51, 4) 행,열
# # 4)
# # print(data2009.head())
# data2009=data2009.drop('Year',axis=1)
# # print(data2009.head())
# data2009=data2009.reset_index()
# # print(data2009.head())
# #5)
# # print('값의 갯수=',data2009.count())
# print('누락값의 갯수=',data2009.shape[0]-data2009.count())
# data2009=data2009.fillna(0)
# # print('값의 갯수=',data2009.count())
# # 6)
# data2009['total']=data2009['Beer']+data2009['Wine']+data2009['Spirits']
# print(data2009.head())
# # 7)
# usa=pd.read_csv('data\\usa.csv')
# usa['country']='미국'
# print(usa.head())
# # 8)
# # df=pd.merge(data2009,usa,on='State')
# # df=df.set_index('State')
# # print(df)
# # 9)
# canada=pd.read_csv('data\\canada.csv')
# canada['country']='캐나다'
# print(canada.head())
# # 10)
# pop=pd.concat([usa,canada],ignore_index=True)
# pop=pop.set_index(['country','State'])
# pop=pop.sort_index()
# print(pop)
# set_index(컬럼명)  :지정된 컬럼으로 인덱스지정, 기존인덱스는 삭제됨
# reset_index() :일련번호로 인덱스 지정,기존인덱스는 컬럼이 된다
# reindex([인덱스 순서]) :현재 인덱스 순서 변경 예)월화수목금토일
# ----탐색적데이터분석--------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager,rc
# fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
# rc('font',family=fontname)
# data=pd.read_csv('data\\rtest.csv')
# # 1)
# # print(data.dtypes)
# # print(data.shape)
# # 2)
# # print(data.head())
# def getResident2(x):
#     if x==1:
#         return '서울'
#     elif x==2:
#         return '인천'
#     elif x==3:
#         return '대전'
#     elif x==4:
#         return '대구'
#     else:
#         return '시군구'
# data['resident2']=data['resident'].apply(getResident2)
# print(data.head())
# # 3)
# # print(data.shape)
# data=data[data['age'].notnull()]
# # print(data.shape)
# # 4)
# # print(data['age'].min())
# # print(data['age'].max())
# # print(data['age'].mean())
# # 5)
# # plt.boxplot(data['age'])
# # plt.title('age')
# # plt.show()
# # 6)
# def getAge2(x):
#     if x<30:
#         return '청년층'
#     elif 31<=x<=55:
#         return '청년층'
#     elif x>=56:
#         return '장년층'
# data['age2']=data['age'].apply(getAge2)
# # print(data.head())
# # 7)
# def getGender2(x):
#     if x==1:
#         return '남자'
#     elif x==2:
#         return '여자'
# data['gender2']=data['gender'].apply(getGender2)
# # print(data.head())
# # 8)
# s1=data.groupby('gender2').size()
# # s1=data.groupby('gender2')['gender2'].count()
# print(s1)
# # 9)
# # plt.pie(s1,labels=s1.index)
# # plt.title('남녀의 빈도수')
# # plt.show()
# # 10)
# plt.scatter(data['age'],data['price'])
# plt.show()
# ---빅데이터 분석 결과 시각화
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)
import seaborn as sns
# 1)
# 2)
data=pd.read_csv('data\\report.csv')
# data.info()
# print(data.head(10))
# print(data.tail(10))
# 3)
# print(data[data['State']=='New Hampshire'])
# plt.scatter(data[data['State']=='New Hampshire']['Beer'],
#             data[data['State']=='New Hampshire']['Wine'])
# plt.show()
# 4)
# plt.style.use('ggplot')
# plt.plot(data[data['State']=='New Hampshire']['Year'],
#          data[data['State']=='New Hampshire']['Beer'])
# plt.plot(data[data['State']=='Utah']['Year'],
#          data[data['State']=='Utah']['Beer'])
# plt.legend(['New Hampshire','Utah'])
# plt.title('주별 맥주 소비량의 변화')
# plt.xlabel('년도')
# plt.ylabel('맥주소비량')
# plt.show()
# 5)
tips=sns.load_dataset('tips')
print(tips.dtypes)
# 6)
# print(tips['total_bill'].min())
# print(tips['total_bill'].max())
# print(tips['total_bill'].mean())
# print(tips['total_bill'].median())
# plt.boxplot(tips['total_bill'])
# plt.show()
# 7)
# p1=pd.pivot_table(tips,index='size',columns='day',values='total_bill',
#                   aggfunc='sum')
# print(p1)
# 8)
# plt.plot(p1.index,p1)
# plt.legend(p1.columns)
# plt.xlabel('좌석수')
# plt.ylabel('식사비용')
# plt.title('식사비용현황')
# plt.show()
# 9)
bank=pd.read_csv('data\\bank.csv',
        parse_dates=['Closing Date','Updated Date'])
# bank.info()
# print(bank.head())
# 10)
bank['yy']=bank['Closing Date'].dt.year
print(bank.head())
s1=bank.groupby('yy').size()
print(s1)
plt.plot(s1)
plt.show()





