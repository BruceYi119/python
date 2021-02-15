import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 과제
# 1)x값이 -10,-20일때의 값을 예측하여 출력하세요
xdata = np.random.rand(100,1)
xdata = xdata * 4 - 20
print(xdata)
ydata = 3 * xdata - 2
ydata = ydata + np.random.randn(100,1)
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1]),tf.float32)
b = tf.Variable(tf.random_normal([1]),tf.float32)
h = w * x + b
cost = tf.reduce_mean(tf.square(h-y))
train = tf.train.GradientDescentOptimizer(0.005).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(501):
        sess.run(train, feed_dict = { x: xdata, y: ydata })
        if i % 50 == 0:
            tempcost, tempw, tempb = sess.run([cost,w,b],feed_dict = { x: xdata, y: ydata })
            temph = sess.run(h, feed_dict = { x: xdata })
            plt.plot(xdata, ydata, 'o')
            plt.plot(xdata, temph)
            plt.show()