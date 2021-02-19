import os
import numpy as np
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

# data=np.loadtxt('data\\zoo\\zoo.csv',delimiter=',')
# # print(data)
# ydata=data[:10,-1:]
# # print(ydata)
# y=tf.placeholder(tf.int64,[None,1])
# onehot1=tf.one_hot(y,7)    #0-6
# onehot2=tf.reshape(onehot1,[-1,7])
# argmax1=tf.argmax(onehot2,1)
# argmax2=tf.reshape(argmax1,[-1,1])
# equal1=tf.equal(y,argmax2)   #True,False   [T,T,F]  2/3
# cast1=tf.cast(equal1,tf.float32)   #[1,1,0]
# mean1=tf.reduce_mean(cast1)
# sess=tf.Session()
# print('y=',sess.run(y,feed_dict={y:ydata}))
# print('onehot1=',sess.run(onehot1,feed_dict={y:ydata}))
# print('onehot2=',sess.run(onehot2,feed_dict={y:ydata}))
# print('argmax1=',sess.run(argmax1,feed_dict={y:ydata}))
# print('argmax2=',sess.run(argmax2,feed_dict={y:ydata}))
# print('equal1=',sess.run(equal1,feed_dict={y:ydata}))
# print('cast1=',sess.run(cast1,feed_dict={y:ydata}))
# print('mean1=',sess.run(mean1,feed_dict={y:ydata}))
# sess.close()
# ------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# data=pd.read_csv('data\\wine.csv',sep=';')
# print(data)
# s1=data.groupby('quality').size()
# print(s1)
# plt.plot(s1)
# plt.show()
# plt.savefig('img\\wine.png')
# ----------------
# a=np.array([[1,2,3],[4,5,6],[7,8,5]])
# print(a)
# print(a[:,-1])
# 5보다 작은 경우  0
# 5이상 8이하     9
# print('1번',a[:,-1]<5)
# print('2번',a[a[:,-1]<5])
# print(a[a[:,-1]<5,-1])
# a[a[:,-1]<5,-1]=0
# print('3번',a)
# a[(a[:,-1]>=5) & (a[:,-1]<=8),-1]=9
# print('4번',a)
# ------------------------------
# 와인의 품질 <=4      -->0
#           <4<=7    -->1
#           >7       -->2
# data=np.loadtxt('data\\wine.csv',delimiter=';',skiprows=1)
# # print(data)
# data[data[:,-1]<=4,-1]=0
# data[(data[:,-1]>4)&(data[:,-1]<=7),-1]=1
# data[data[:,-1]>7,-1]=2
# # print(data)
# # print(data[:,-1])
# np.savetxt('data\\wine2.csv',data)
# --------------
# data=pd.read_csv('data\\wine2.csv',sep=' ',header=None)
# print(data)
# s1=data.groupby(11).size()
# print(s1)
# --------------------
# # 70%의 데이터로 학습,30%의 데이터로 검증----
# data=np.loadtxt('data\\wine2.csv')
# print(data.shape)  #(4898, 12)
# np.random.shuffle(data)
# trainx,trainy=data[:3429,:11],data[:3429,11:]
# testx,testy=data[3429:,:11],data[3429:,11:]
# print(testy)  #0,1,2....
# x=tf.placeholder(tf.float32,[None,11])
# y=tf.placeholder(tf.int32,[None,1])
# onehot=tf.one_hot(y,3)   #3차원
# onehot2=tf.reshape(onehot,[-1,3])
# w=tf.Variable(tf.random_normal([11,3]))
# b=tf.Variable(tf.random_normal([3]))
# logits=tf.matmul(x,w)+b
# h=tf.nn.softmax(logits)
# cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
#     logits=logits,labels=onehot2))
# train=tf.train.GradientDescentOptimizer(0.0005).minimize(cost)
# corr=tf.equal(tf.argmax(h,1),tf.argmax(onehot2,1))
# acc=tf.reduce_mean(tf.cast(corr,tf.float32))
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(5001):
#         sess.run(train,feed_dict={x:trainx,y:trainy})
#         if i%1000==0:
#             print(sess.run(cost,feed_dict={x:trainx,y:trainy}))
#     print('정확도=',sess.run(acc,feed_dict={x:testx,y:testy}))
# 0.01   3.5034807
# 0.001  0.4899125
# 0.0003 0.53252804
# 0.0005  0.33876505
# 0.0001   1.9680853
# -------------------------------
# data.kma.go.kr
# data=pd.read_csv('data\\temp.csv',engine='python',parse_dates=['일시'])
# # print(data)
# # print(data.info())
# data['yy']=data['일시'].dt.year
# data['mm']=data['일시'].dt.month
# data['dd']=data['일시'].dt.day
# data=data.drop(['일시'],axis=1)
# data.columns=['temp','yy','mm','dd']
# print(data)
# data=data.sort_values(['yy','mm','dd'])
# data.to_csv('data\\temp2.csv',index=False)
# 일별평균기온
# data=pd.read_csv('data\\temp2.csv')
# print(data)
# s1=data.groupby(['mm','dd'])['temp'].mean()
# print(s1)
# plt.plot(s1.values)
# plt.show()
# 년도별로 기온이 -10이하인날
# cool=data[data['temp']<=-10]
# print(cool)
# s2=cool.groupby('yy').size()
# print(s2)
# 6일치의 온도데이터를 읽어 7일째의 기온예측--------
# 70%의 데이터로 학습,30%의 데이터로 검증----
def makedata(a):
    interval=6
    xdata=[]
    ydata=[]
    for i in range(len(a)):
        if i<interval:
            continue
        ydata.append(a[i])
        temp=[]
        for j in range(interval):
            z=i-interval+j
            temp.append(a[z])
        xdata.append(temp)
    return xdata,ydata
data=np.loadtxt('data\\temp2.csv',delimiter=',',skiprows=1)
print(data)
train=data[data[:,1]<=2017,:]
test=data[data[:,1]>2017,:]
# print(test)
trainx,trainy=makedata(train[:,0])
testx,testy=makedata(test[:,0])
# print(trainx)
# print(trainy)   #리스트1차원
trainy=np.array(trainy).reshape(-1,1)
# print(trainy)   #넘파이배열 2차원
testy=np.array(testy).reshape(-1,1)
x=tf.compat.v1.placeholder(tf.float32,[None,6])
y=tf.compat.v1.placeholder(tf.float32,[None,1])
w=tf.Variable(tf.compat.v1.random_normal([6,1]))
b=tf.Variable(tf.compat.v1.random_normal([1]))
h=tf.matmul(x,w)+b
cost=tf.reduce_mean(tf.square(h-y))
train=tf.compat.v1.train.GradientDescentOptimizer(0.0003).minimize(cost)
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for i in range(5001):
        sess.run(train,feed_dict={x:trainx,y:trainy})
        if i%1000==0:
            print(sess.run(cost,feed_dict={x:trainx,y:trainy}))
#     검증하기
    result=sess.run(h,feed_dict={x:testx,y:testy})
plt.plot(testy)
plt.plot(result)
plt.show()

# # 3개의 데이터를 읽어 4번째 데이터를 예측
# a=[0,1,2,3,4,5,6,7,8,9]
# # x=[[0,1,2],[1,2,3],[2,3,4]]
# # y=[3,4,5]
# interval=3
# x=[]
# y=[]
# for i in range(len(a)):   #i=0,1,2...
#     if i<interval:
#         continue
#     tempx=[]
#     for j in range(interval):   #i=3   0,1,2
#         z=i-interval+j
#         tempx.append(a[z])
#     x.append(tempx)
#     y.append(a[i])
# print('x=',x)
# print('y=',y)