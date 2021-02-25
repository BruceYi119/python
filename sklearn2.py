import os
import random
import pandas as pd
import sklearn as sk
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

# colors = [['red','green','blue','orange'],['pink','ivory','purple','tomato']]
# data = pd.DataFrame(colors, columns=['a','b','c','d'])

# for k,v in data.iteritems():
#     print(k)        # 열이름
#     print(v)        # 행번호, 값

# for k,v in data.iterrows():
#     print(k)        # 행인덱스
#     print(v)        # 값

# for t in data.itertuples():
#     print(t)        # 행인덱스와 값이 튜플

# mr = pd.read_csv(os.path.join('data','mushroom.csv'), header=None)
# data = []
# label = []

# for k,v in mr.iterrows():
#     label.append(v[0])
#     temp = []
#     for d in v.iloc[1:]:
#         temp.append(ord(d))
#     data.append(temp)

# x_train, x_test, y_train, y_test = train_test_split(data, label, train_size=0.75, shuffle=True)
# model = RandomForestClassifier()
# model.fit(x_train, y_train)
# pred = model.predict(x_test)
# print('정확도 =', accuracy_score(pred, y_test))

# 교차검증 (데이터가 적을때)
iris = pd.read_csv(os.path.join('data','iris.csv'), skiprows=1, header=None)

x = []
y = []
for k,v in iris.iterrows():
    temp = []
    y.append(v[4])
    temp.append(float(v[0]))
    temp.append(float(v[1]))
    temp.append(float(v[2]))
    temp.append(float(v[3]))
    x.append(temp)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75, shuffle=True)

model = SVC()
modelLr = LogisticRegression()
modelDt = DecisionTreeClassifier(random_state=0)

model.fit(x_train, y_train)
# modelLr.fit(x_train, y_train)
# modelDt.fit(x_train, y_train)
pred = model.predict(x_test)
print('정확도 =',accuracy_score(pred, y_test))
# pred = modelLr.predict(x_test)
# print('정확도 =',accuracy_score(pred, y_test))
# pred = modelDt.predict(x_test)
# print('정확도 =',accuracy_score(pred, y_test))
# scores = cross_val_score(modelLr, x_test, y_test)
# print('정확도 =', scores)
# scores = cross_val_score(modelDt, x_test, y_test)
# print('정확도 =', scores)

#############################################################

# def split_x_y(data):
#     x=[]
#     y=[]
#     for d in data:
#         x.append(d[:4])
#         y.append(d[4])
#     return x,y
# data=open('data\\iris.csv').read().split('\n')
# # print(data)
# del data[0]
# # print(data)
# csv=[]
# for line in data:
#     temp=[]
#     line=line.split(',')
#     print(line)  #['5.1', '3.5', '1.4', '0.2', 'setosa']
#     temp.append(float(line[0]))
#     temp.append(float(line[1]))
#     temp.append(float(line[2]))
#     temp.append(float(line[3]))
#     temp.append(line[4])
#     # print(temp)
#     csv.append(temp)
# # print(csv)
# # 데이터분할
# k=5
# #[[],[],[],[],[]]
# csvk=[[] for i in range(k)]   #[[], [], [], [], []]
# # print(csvk)
# for i in range(len(csv)): #i=0,1,...149
#     csvk[i%k].append(csv[i])
# # print(csvk)
# # print(len(csvk))   #5
# # print(len(csvk[0]))   #30
# scores=[]
# for testdata in csvk:
#     print('검증용data=',testdata)   #2차원
#     traindata=[]
#     for i in csvk:
#         if i!=testdata:
#             # traindata.append(i)
#             traindata=traindata+i
#     # print('훈련용data=',traindata)   #2차원
#     testx,testy=split_x_y(testdata)
#     trainx,trainy=split_x_y(traindata)
#     # print('testx=',testx)
#     # print('testy=',testy)
#     # 모델생성
#     model=SVC()
#     model.fit(trainx,trainy)
#     pred=model.predict(testx)
#     # print('정확도=',accuracy_score(pred,testy))
#     scores.append(accuracy_score(pred,testy))
# print('정확도=',scores)
# print('전체정확도=',sum(scores)/len(scores))


# a=[1,2,3]
# b=['one','two','three']
# a.append(b)
# print('1번',a)
# print('2번',a+b)
# ------------------------
# a=['one','two','three','four','five','six']
# k=3
# csvk=[[] for i in range(k)]
# print(csvk)
# for i in range(len(a)):
#     csvk[i%k].append(a[i])   #i%4-->0,1,2
# print(csvk)
# [['one', 'four'], ['two', 'five'], ['three', 'six']]
# for testdata in csvk:
#     print('검증용data=',testdata)
#     traindata=[]
#     for i in csvk:
#         if i!=testdata:
#             traindata=traindata+i
#     print('훈련용data=', traindata)