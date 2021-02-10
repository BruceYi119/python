from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
data = input_data.read_data_sets("../mnist/data/", one_hot = True)
# print(data.train) #학습용 데이터
# print(data.test) #검증용 데이터
# print('학습용데이터 갯수', data.train.num_examples) #55000
# print('학습용데이터의 첫번째 데이터', data.train.labels[0 : 1]) #7
# print('학습용데이터의 실제이미지', data.train.images[0 : 1])
# print('학습용데이터의 실제이미지', data.train.images[0 : 1].shape)
plt.imshow(data.train.images[0:1].reshape(28, 28), cmap = 'Greys', interpolation = 'nearset')
plt.show()