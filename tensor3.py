import tensorflow as tf      #1.5.0
import numpy as np
# # # iris1.csv데이터를 읽어 다음을 진행하시오
# # # 1) 앞쪽 4개의 모든 열은 xdata, 마지막 3개의 열은 ydata에 넣으시오
# data=np.loadtxt('data\\iris1.csv',skiprows=1,delimiter=',')
# # print(data)
# # print(data.shape)
# xdata=data[:,:4]
# ydata=data[:,4:]
# # print(xdata)
# # print(ydata)
# # # 2) 실행시에 x에 xdata, y에 ydata값을 넣어 서
# # # y의 값을 원래의 값으로 복원하여 출력하시오 (100 ->0, 010->1)
# x=tf.placeholder(tf.float32,[150,4])
# y=tf.placeholder(tf.float32,[150,3])
# op1=tf.argmax(y,1)
# with tf.Session() as sess:
#     print(sess.run(op1,feed_dict={y:ydata}))
# ----------------------
# # setosa      -> 0
# # versicolor  -> 1
# # virginica   -> 2
# data=np.loadtxt('data\\iris2.csv',delimiter=',',skiprows=1)
# print(data.shape)
# xdata=data[:,:4]
# ydata=data[:,4:]
# print(ydata.shape)   #(150, 1)
# print(ydata)
# # y=tf.placeholder(tf.int32,[150,1])   #2차원
# y=tf.placeholder(tf.int32,[None,1])   #2차원
# onehot=tf.one_hot(y,3)   #3차원
# onehot2=tf.reshape(onehot,[-1,3])   #2차원
# with tf.Session() as sess:
#     # print(sess.run(onehot,feed_dict={y:ydata}))
#     # print(sess.run(onehot2,feed_dict={y:ydata}))
#     #새로운 데이터 입력
#     print(sess.run(onehot2,feed_dict={y:[[0],[2]]}))
# -------------
# from tensorflow.examples.tutorials.mnist import input_data
# import matplotlib.pyplot as plt
# data=input_data.read_data_sets("../mnist/data/",one_hot=True)
# print(data.train)   #학습용 데이터
# print(data.test)    #검증용 데이터
# # print('학습용데이터 갯수',data.train.num_examples)   #55000
# # print('학습용데이터의 첫번째 데이터',data.train.labels[0:1] )   #7
# # print('학습용데이터의 실제이미지',data.train.images[0:1])   #넘파이배열
# # plt.imshow(data.train.images[0:1].reshape(28,28),cmap='Greys',interpolation='nearest')
# # plt.show()
# print('학습용데이터의 오만번째 데이터',data.train.labels[49999:50000] )
# print('학습용데이터의 실제이미지')
# plt.imshow(data.train.images[49999:50000].reshape(28,28),cmap='Greys',interpolation='nearest')
# plt.show()
#iris --> setosa(0), versicolor(1), virginica(2)   분류(다중)
#mnist -->0,1,2,..9    다중분류
#아빠키 -->아들키 예측    수치 175.6