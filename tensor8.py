import os
import random
import numpy as np
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
import matplotlib.pyplot as plt
# from tensorflow.examples.tutorials.mnist import input_data            # v1버전 mnist

# mnist = input_data.read_data_sets('../mnist/data', one_hot=True)      # v1버전 mnist
# v1 버전
# print('학습데이터셋',mnist.train)
# print('검증데이터셋',mnist.test)
# print('학습데이터 개수',mnist.train.num_examples)  #55000
# print('검증데이터 개수',mnist.test.num_examples)   #10000
# print('학습데이터 5000번째 데이터',mnist.train.images[4999:5000])
# print('학습데이터 5000번째 데이터정답',mnist.train.labels[4999:5000])
# plt.imshow(mnist.train.images[4999:5000].reshape(28,28),cmap='Greys',
#            interpolation='nearest')
# plt.show()
# print('검증데이터 5000번째 데이터',mnist.test.images[4999:5000])
# print('검증데이터 5000번째 데이터정답',mnist.test.labels[4999:5000])
# print('검증데이터 5000번째 데이터 차원',mnist.test.images[4999:5000].shape)
# plt.imshow(mnist.test.images[4999:5000].reshape(28,28),
#            cmap='Greys', interpolation='nearest')
# plt.show()
# x = tf.compat.v1.placeholder(tf.float32,[None,784])
# y = tf.compat.v1.placeholder(tf.float32,[None,10])
# w = tf.Variable(tf.compat.v1.random_normal([784,10]))
# b = tf.Variable(tf.compat.v1.random_normal([10]))
# logits = tf.matmul(x,w) + b
# h = tf.nn.softmax(logits)
# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
# train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)
# corr = tf.equal(tf.argmax(h,1),tf.argmax(y,1))
# acc = tf.reduce_mean(tf.cast(corr,tf.float32))
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(2001):
#         batchx,batchy = mnist.train.next_batch(100)
#         sess.run(train, feed_dict = { x: batchx, y: batchy })
#         if i % 500 == 0:
#             print(sess.run(acc, feed_dict = { x: mnist.train.images, y: mnist.train.labels }))
#             # 정확도가 점차 높아짐
#             print(sess.run(cost, feed_dict = { x: mnist.train.images, y: mnist.train.labels }))
#             # cost가 점차 작아짐
#     # 평가
#     print('정확도=',sess.run(acc, feed_dict = { x: mnist.test.images, y: mnist.test.labels }))
#     #예측
#     r = random.randint(0, mnist.test.num_examples-1)  #0~9999
#     print('실제정답 :', sess.run(tf.argmax(mnist.test.labels[r:r+1],1)) )
#     print('예측값:',sess.run(tf.argmax(h,1), feed_dict = { x: mnist.test.images[r:r+1] }))
#     plt.imshow(mnist.test.images[r:r+1].reshape(28,28), cmap = 'Greys', interpolation = 'nearest')
#     plt.show()

# v2 버전
# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test), images = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0

# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28)),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dropout(0.2),
#   tf.keras.layers.Dense(10, activation='softmax')
# ])

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=5)
# model.evaluate(x_test, y_test, verbose=2)

# fashtion_mnist = tf.keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = fashtion_mnist.load_data()

# plt.figure()
# plt.imshow(train_images[9])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# train_images = train_images / 255.0
# test_images = test_images / 255.0
# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_labels[i]])
# plt.show()

data = np.loadtxt(os.path.join('data','diabetes.csv'), delimiter=',')
# v1 버전
# print(data.shape)
# 75%학습, 25%검증 (데이터 (759, 9)) 759 * 0.75 = 569
x_train = data[:569,:-1]
y_train = data[:569,-1:]
# print(x_train.shape)
# print(y_train.shape)
x_test = data[569:,:-1]
y_test = data[569:,-1:]
x = tf.compat.v1.placeholder(tf.float32, [None,8])
y = tf.compat.v1.placeholder(tf.float32, [None,1])
w = tf.Variable(tf.compat.v1.random_normal([8,1]))
b = tf.Variable(tf.compat.v1.random_normal([1]))
logits = tf.matmul(x,w) + b
h = tf.sigmoid(logits)
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=y))
train = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(cost)

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    for i in range(7001):
        sess.run(train, feed_dict={ x: x_train, y: y_train })
        if i % 1000 == 0:
            print(sess.run(cost, feed_dict={ x: x_train, y: y_train }))

    # 예측
    pred = tf.cast(h > 0.5, tf.float32)
    print('예측값=', sess.run(pred, feed_dict={ x: x_test }))
    # 평가
    acc = tf.reduce_mean(tf.cast(tf.equal(pred,y), tf.float32))
    print('정확도=', sess.run(acc, feed_dict={ x: x_test, y: y_test }))