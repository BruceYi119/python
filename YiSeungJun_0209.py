import os
import numpy as np
import tensorflow as tf

data = np.loadtxt(os.path.join('data','iris1.csv'), skiprows=1, delimiter=',')
x = tf.placeholder(tf.float32, [None,4], name='x')
y = tf.placeholder(tf.float32, [None,3], name='y')
xdata = x
ydata = y
resety = tf.argmax(y,1)

# 1) 앞쪽 4개의 모든 열은 xdata, 마지막 3개의 열은 ydata에 넣으시오
# 2) 실행시에 x에 xdata, y에 ydata값을 넣어 서
# y의 값을 원래의 값으로 복원하여 출력하시오 (100 ->0, 010->1)
with tf.Session() as sess:
    print(sess.run(xdata, feed_dict={ x: data[:,:4] }))
    print(sess.run(ydata, feed_dict={ y: data[:,4:] }))
    print(sess.run(resety, feed_dict={ y: data[:,4:] }))