import os
import glob
# import sklearn
import numpy as np
import pandas as pd
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# https://scikit-learn.org/stable/tutorial/machine_learning_map/

# x_train = [[0,0],[0,1],[1,0],[1,1]]
# y_train = [0,0,0,1]

# 모델생성
# model = LinearSVC()
# 학습
# model.fit(x_train,y_train)
# 예측
# x_test = [[0,0],[0,1],[1,0],[1,1]]
# pred = model.predict(x_test)
# 평가
# print('정확도 =',accuracy_score([0,0,0,1],pred))

# data = pd.read_csv(os.path.join('data','iris.csv'))
# 데이터와 정답으로 분리
# x = data.loc[:,['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']]
# y = data.loc[:,'Species']

# 70%데이터로 훈련,30%데이터로 검증
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=True)
# model = SVC()
# model.fit(x_train, y_train)
# pred = model.predict(x_test)
# print('정확도 =', accuracy_score(y_test, pred))

# x = np.random.rand(100,1)  #0-1사이의 숫자 100개
# print(x)
# x = x*4-2      # -2<=x<=2
# print(x)
# y = 3 * x - 2 + np.random.randn(100,1)
# plt.plot(x,y,'o')
# plt.show()
# 모델생성
# model = linear_model.LinearRegression()
# 훈련
# model.fit(x,y)
# print('기울기 =', model.coef_)
# print('절편 =', model.intercept_)
# 예측
# pred = model.predict(x)
# plt.plot(x, y, 'o')
# plt.plot(x, pred)
# plt.show()
# ---------------------------------
# data = pd.read_csv(os.path.join('data','cars.csv'))
# print(data)
# print(list(data['speed']))
# x = []
# y = []
# for i in range(data.shape[0]):
#     print(list(data['speed'])[i])
#     x.append([list(data['speed'])[i]])
#     y.append([list(data['dist'])[i]])
# print(x)
# print(y)
# model = linear_model.LinearRegression()
# model.fit(x, y)
# print('기울기 =', model.coef_)
# print('절편 =', model.intercept_)
# plt.plot(x, y, 'o')             # 실제데이터
# plt.plot(x,model.predict(x))    # 모델
# plt.show()

# print(ord('a'))
# print(ord('A'))
# print(chr(65))
# print(sum([1,2,3,4,5]))
# print('adHdsf123'.lower())
# print('adHdsf123'.upper())

# def make_data(f):
#     with open(f, encoding='utf-8') as f:
#         text = f.read().lower()
#         # print(text)
#         cnt = [0 for i in range(26)]
#         # print(cnt)
#         # str = 'alice!^^ css3'
#         for c in text:
#             n = ord(c)
#             if ord('a') <= n < ord('z'):
#                 cnt[n - ord('a')] = cnt[n - ord('a')] + 1
#         # print(cnt)
#         total = sum(cnt)
#         # print(total)
#         data = list(map(lambda i:i / total, cnt))
#         # print(data)
#         return data

# def load_files(path):
#     labels = []
#     data = []
#     for f in glob.glob(path):
#         # print(os.path.dirname(f))
#         # print(os.path.basename(f))
#         # print(os.path.basename(f)[:2])
#         labels.append(os.path.basename(f)[:2])
#         data.append(make_data(f))
#     return data, labels

# x, y = load_files(os.path.join('data','lang','train','*.txt'))
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=True)
# model = SVC()
# model.fit(x,y)
# pred = model.predict(x_test)
# print('정확도 =', accuracy_score(y_test, pred))

data = pd.read_csv(os.path.join('data','water.csv'))
x = data.loc[:,['old','new']]
y = data.loc[:,'as_time']
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=False)
# model = SVC()
# model.fit(x,y)
# pred = model.predict(x_test)
# print('정확도 =', accuracy_score(y_test, pred))

model = LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.intercept_)
# 월말 최종 대여수를 보니 총 대여수가 300,000대, 그중 10년 이상
# 노후 정수기 대수가 70,000대로 집계되었다.
# 다음달의 AS시간을 예측하고 그에 따라 필요한 AS기사의 인원수를 예측하시오
print('예측as시간 =', model.predict([[70000,230000]]))