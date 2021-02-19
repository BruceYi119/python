import os
import numpy as np
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

# diabetes = load_diabetes()
# print(diabetes.data.shape)
# print(diabetes.target.shape)
# print(diabetes.data[:3])
# print(diabetes.target[:3])
# xdata = diabetes.data[:,2]
# ydata = diabetes.target
# plt.plot(xdata, ydata, 'o')
# plt.show()

# print(xdata[:10])
# print(ydata[:10])

# w = 1.0
# b = 1.0
# h = xdata[0] * w + b
# print('예측값 h=',h)
# print('정답 ydata=',ydata[0])

# w를 0.1 증가 -->h값 변화?
# winc = w + 0.1
# hinc = xdata[0] * winc + b
# print('예측값 hinc=',hinc)
# wrate = (hinc - h) / (winc - w)
# ((xdata[0] * winc + b) - (xdata[0] * w + b)) / (winc - w) =
# (xdata[0] * winc + b - xdata[0] * w - b) / (winc - w) =
# (xdata[0] * winc - xdata[0] * w) / (winc - w) =
# xdata[0] * (winc - w) / (winc - w) = xdata[0]
# print('wrate = ',wrate)   #xdata[0]
# wnew = w + wrate
# print('wnew = ', wnew)
# 경사하강법 : 모델이 데이터를 잘 표현할 수 있도록
# 기울기를 사용하여 모델을 조금씩 조정하는 알고리즘
# 절편 업데이터
# binc = b + 0.1
# hinc = xdata[0] * w +binc
# print('절편값의 변화에 따른 hinc = ', hinc)
# brate = (hinc - h) / (binc - b)
# print('brate = ', brate)
# bnew = b + brate
# print('bnew = ', bnew)
# 오차역전파 :예측값과 정답의 차이를 이용하여 w와 b를 업데이트--------------
# 오차가 연이어 전파되는 모습
# err=ydata[0]-h
# wnew = w + wrate * err
# bnew=b + brate * err
# print('wnew = ', wnew, 'bnew = ', bnew)
# 두번째 샘플에 적용
# h = xdata[1] * wnew + bnew
# print('예측값 = ', h, '정답 = ', ydata[1])
# err = ydata[1] - h
# wrate = xdata[1]
# wnew = wnew + wrate * err
# bnew = bnew + brate * err
# print('wnew = ', wnew, 'bnew = ', bnew)
# for xi,yi in zip(xdata, ydata):
#     h = xi * w + b
#     err = yi - h
#     wrate = xi
#     w = w + wrate * err
#     b = b + 1 * err
# print('w = ', w, 'b = ', b)
# plt.plot(xdata, ydata, 'o')
# left = -0.1 * w + b
# right = 0.2 * w + b
# plt.plot([-0.1,0.2], [left,right])
# plt.show()
# 에포크(epoch) : 한단위의 작업을 진행하는것
# 여러 에포크 반복
# for i in range(1000):
#     for xi, yi in zip(xdata, ydata):
#         h = xi * w + b
#         err = yi - h
#         wrate = xi
#         w = w + wrate * err
#         b = b + 1 * err
# print('w = ', w, 'b = ',b)
# plt.plot(xdata,ydata,'o')
# left = -0.1 * w + b
# right = 0.2 * w + b
# plt.plot([-0.1,0.2], [left,right])
# plt.show()

data = np.loadtxt(os.path.join('data', 'iris1.csv'), delimiter=',', skiprows=1)
# print(data)
# print(data.shape)
# 70%의 데이터로 학습,30%의 데이터로 검증
np.random.shuffle(data)
trainx,trainy=data[:105,:4],data[:105,4:]
# print(trainx.shape)   #(105, 4)   학습용데이터
# print(trainy.shape)   #(105, 3)   학습용데이터 정답
testx,testy=data[105:,:4],data[105:,4:]
# print(testx.shape)   #(45, 4)    검증용데이터
# print(testy.shape)   #(45, 3)    검증용데이터 정답
# print(testy)
x = tf.compat.v1.placeholder(tf.float32,[None,4])
y = tf.compat.v1.placeholder(tf.float32,[None,3])
w = tf.Variable(tf.compat.v1.random_normal([4,3]))
#[None,4] X[4,3]=[None,3]
b = tf.Variable(tf.compat.v1.random_normal([3]))
logits = tf.matmul(x,w) + b
h = tf.nn.softmax(logits)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(cost)
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    # 학습하기
    for i in range(3001):
        sess.run(train,feed_dict={x:trainx,y:trainy})
        if i%1000==0:
            print(sess.run(cost,feed_dict={x:trainx,y:trainy}))
    # print(sess.run([w,b]))
    # 검증하기
    pred = sess.run(h, feed_dict={x:testx})
    corr=tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
    acc=tf.reduce_mean(tf.cast(corr,tf.float32))
    print('정확도 = ', sess.run(acc, feed_dict={x:testx, y: testy}))

# w = tf.Variable(tf.ones(shape=(2,2)), name="w")
# b = tf.Variable(tf.zeros(shape=(2)), name="b")
# @tf.function
# def h(x):
#     return w * x + b
#
# x = h([1,0])
# print(x)