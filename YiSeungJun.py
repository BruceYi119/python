import os
import numpy as np
import pandas as pd
import tensorflow as tf
# import matplotlib.pyplot as plt
# from sklearn import linear_model
tf.compat.v1.disable_eager_execution()

data = pd.read_csv(os.path.join('data', 'water.csv'))

# 1-1
x_train = np.array(data.loc[:, ['old', 'new']])
x_test = np.array(data.loc[:, ['old', 'new']])
y_train = np.array(data.loc[:, 'as_time']).reshape(-1,1)
y_test = np.array(data.loc[:, 'as_time']).reshape(-1,1)
x = tf.compat.v1.placeholder(tf.float32, [None, 2])
y = tf.compat.v1.placeholder(tf.float32, [None, 1])
w = tf.Variable(tf.compat.v1.random_normal([2, 1]))
b = tf.Variable(tf.compat.v1.random_normal([1]))
logits = tf.matmul(x, w) + b
h = tf.sigmoid(logits)
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=y))
train = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(cost)

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for i in range(5001):
        sess.run(train, feed_dict={x:x_train,y:y_train})
        if i % 1000 == 0:
            print('cost =', sess.run(cost, feed_dict={x: x_train, y: y_train}))
    print('w =', sess.run(w), 'b =', sess.run(b))

# 1-2
data = np.loadtxt(os.path.join('data','water.csv'), delimiter=',', skiprows=1)
xdata = data[:,1:3]
ydata = data[:,-1:]
x = tf.compat.v1.placeholder(tf.float32,[None,2])
y = tf.compat.v1.placeholder(tf.float32,[None,1])
w = tf.Variable(tf.compat.v1.random_normal([2,1]))
b = tf.Variable(tf.compat.v1.random_normal([1]))
h = tf.matmul(x, w) + b
cost = tf.reduce_mean(tf.square(y - h))
train = tf.compat.v1.train.GradientDescentOptimizer(0.00000000003).minimize(cost)
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for i in range(5001):
        sess.run(train,feed_dict={x:xdata,y:ydata})
        if i % 1000 == 0:
            print(sess.run(cost,feed_dict={x:xdata,y:ydata}))

    print('필요 일원 수 =', sess.run(h, feed_dict={x:[[80000, 270000]]}) / (8 * 20))

# 2
data = np.loadtxt(os.path.join('data', 'iris1.csv'), delimiter=',', skiprows=1)
np.random.shuffle(data)
x_train, y_train = data[:105,:4],data[:105,4:]
x_test, y_test = data[105:,:4],data[105:,4:]
x = tf.compat.v1.placeholder(tf.float32,[None,4])
y = tf.compat.v1.placeholder(tf.float32,[None,3])
w = tf.Variable(tf.compat.v1.random_normal([4,3]))
b = tf.Variable(tf.compat.v1.random_normal([3]))
logits = tf.matmul(x,w) + b
h = tf.nn.softmax(logits)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(cost)
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for i in range(3001):
        sess.run(train,feed_dict={x:x_train,y:y_train})
        if i % 1000 == 0:
            print(sess.run(cost,feed_dict={x:x_train,y:y_train}))
    pred = sess.run(h, feed_dict={x:x_test})
    corr = tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
    acc = tf.reduce_mean(tf.cast(corr,tf.float32))
    print('정확도 =', sess.run(acc, feed_dict={x:x_test,y:y_test}))