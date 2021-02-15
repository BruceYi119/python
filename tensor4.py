# 공부시간,    성적
#    10      90
#    8       85
#    5       60
#    7       ?    --점수예측  95,92,..,80.5  숫자예측 회귀
#                 --a,b,c..f      다중분류
#                 --pass,fail     이진분류
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# xdata=[1,2,3]
# ydata=[1,2,3]
# w=tf.Variable(tf.random_normal([1]))
# b=tf.Variable(tf.random_normal([1]))
# h=w*xdata+b
# cost=tf.reduce_mean(tf.square(h-ydata))
# train=tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(2001):
#         sess.run(train)
#         if i%100==0:
#             print(i,sess.run(cost),sess.run(w),sess.run(b))
# ---------------
data=np.loadtxt('data\\cars.csv',unpack=True,delimiter=',',skiprows=1)
# print(data)
print(data[0])   #speed  ---xdata
print(data[1])   #dist   ---ydata정답
# plt.plot(data[0],data[1],'o')
# plt.show()
x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)
w=tf.Variable(tf.random_uniform([1],-1,1))
b=tf.Variable(tf.random_uniform([1],-1,1))
h=w*x+b
cost=tf.reduce_mean(tf.square(y-h))
train=tf.train.GradientDescentOptimizer(0.0035).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2001):
        sess.run(train,feed_dict={x:data[0],y:data[1]})
        if i%100==0:
            print(sess.run([cost,w,b],
                   feed_dict={x:data[0],y:data[1]}))
# 0.0035     228.87021
# 0.003      229.6947,
# 0.001      239.9422
# 0.0003   250.25238
# 0.0005     246.66548
# 0.0001     255.51486
# x가 20일때의 제동거리 예측

xdata=np.random.rand(100,1)
xdata=xdata*4-2  #-2~2사이의 값
print(xdata.dtype)
ydata=3*xdata-2
ydata=ydata+np.random.randn(100,1)  #노이즈 추가
x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)
w=tf.Variable(tf.random_normal([1]),tf.float32)
b=tf.Variable(tf.random_normal([1]),tf.float32)
h=w*x+b
cost=tf.reduce_mean(tf.square(h-y))
train=tf.train.GradientDescentOptimizer(0.005).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(501):
        sess.run(train,feed_dict={x:xdata,y:ydata})
        if i%50==0:
            tempcost,tempw,tempb=sess.run([cost,w,b],feed_dict={x:xdata,y:ydata})
            print(tempcost,tempw,tempb)
            temph=sess.run(h,feed_dict={x:xdata})
            plt.plot(xdata,ydata,'o')
            plt.plot(xdata,temph)    #모델
            plt.show()