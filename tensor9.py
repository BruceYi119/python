import numpy as np
import tensorflow as tf
data=np.loadtxt('data\\water.csv',skiprows=1,delimiter=',')
# print(data)
xdata=data[:,1:3]
ydata=data[:,-1:]
# print(xdata)
# print(ydata)
x=tf.placeholder(tf.float32,[None,2])
y=tf.placeholder(tf.float32,[None,1])
w=tf.Variable(tf.random_normal([2,1]))
b=tf.Variable(tf.random_normal([1]))
h=tf.matmul(x,w)+b
# [None,2]X [2,1]=[None,1]
cost=tf.reduce_mean(tf.square(y-h))
train=tf.train.GradientDescentOptimizer(0.00000000003).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5001):
        sess.run(train,feed_dict={x:xdata,y:ydata})
        if i%1000==0:
            print(sess.run(cost,feed_dict={x:xdata,y:ydata}))
# # 월말 최종 대여수를 보니 총 대여수가 300,000대, 그중 10년 이상
# # 노후 정수기 대수가 70,000대로 집계되었다.
# # 다음달의 AS시간을 예측하고 그에 따라 필요한 AS기사의 인원수를 예측하시오
    print(sess.run(h,feed_dict={x:[[70000,230000]]}))



