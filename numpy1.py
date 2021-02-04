import numpy as np
# Numerical Python, 과학계산, 데이터 분석시 사용

# print(np.__version__)
# np.info(항목) 도움말
# np.info(np.array)
# 넘파이 배열 생성:같은 종류의 데이터를 담는 다차원배열(ndarray)
# 변수=np.array(list [,속성])
# li=[1,2,3,4,5]
# print(li)
# a1=np.array(li)
# print(a1)
# print(a1.shape)  #튜플형태(행수,)
# print(a1.dtype)  #데이터타입
# print(type(a1))  #a1의 타입
# print(a1.ndim)  #배열의 차원

# a2=np.array(li,dtype=np.float64)
# print(a2)
# print(a2.dtype)  #데이터타입
# a1=np.array([1,2,3.,4,5])
# print(a1)
# --2차원
# a2=np.array([[1,2,3],[4,5,6]])
# print(a2)
# print(a2.shape)
# --3차원
# a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a3)
# print(a3.shape)
# 초기화함수
# 변수=np.zeros(shape,[속성])
# a1=np.zeros((2,3))
# print(a1)
# a1=np.ones((2,3))
# print(a1)
# a1=np.full((2,3),7)
# print(a1)
# a1=np.empty((3,4))   #기존 메모리에 남아있는 값
# print(a1)
# 단위행렬
# a1=np.eye(3)
# print(a1)
# li=[[1,2,3,4],[5,6,7,8]]
# print(li)
# a1=np.ones_like(li)
# print(a1)
# a1=np.zeros_like(li)
# print(a1)
# # a1=np.full_like(li,3.54)
# a1=np.full_like(li,3.54,dtype=np.float64)
# print(a1)
# a1=np.empty_like(li)
# print(a1)
# 데이터 입출력------------------------------------
# 1.save(파일명,넘파이배열) binary 형태로 저장
# a0=np.zeros((4,3))
# print(a0)
# a1=np.ones((2,3))
# print(a1)
# a7=np.full((5,2),7)
# print(a7)
# np.save('data/a0',a0)
# np.save('data/a1',a1)
# 2.savez() 두개이상의 ndarray를 binary 형태로 저장
# 3.savetxt() text형태로 저장

# 1 변수=load()
# 2 변수=loadtxt(파일명,속성)
# data=np.loadtxt('data/d1.txt')
# print(data)
# print('-'*30)
# # 데이터를 수직으로 읽기
# data=np.loadtxt('data/d1.txt',unpack=True)
# print(data)
# print(type(data))
# print(data[0])  #data[0]=[1. 2. 3.]
# print(data[1])
# print(data[0][0])
# data=np.loadtxt('data/d2.txt',delimiter=',')
# print(data)
# data=np.loadtxt('data/d2.txt',delimiter=',',unpack=True)
# print(data)
# print('-'*30)
# data=np.loadtxt('data/d3.txt',delimiter=',',skiprows=1)
# print(data)
# 파이썬의 range함수의 넘파이버젼 arange()
# print(np.arange(10))
# print(np.arange(10).astype(np.float))  #데이터형변환
# # 슬라이싱, 색인
# a1=np.arange(15)
# print(a1)
# print(a1[5])
# print(a1[5:8])
# a1[5:8]=99
# print('a1=',a1)
# b=a1[5:8]   # 넘파이에서 배열의 조각은 원본의 뷰
# print('b=',b)
# b[1]=100
# print('b=',b)
# print('a1=',a1)
# print('-'*30)
# c=a1[5:8].copy() #원본 배열의 복사본
# print('c=',c)
# c[2]=101
# print('a1=',a1)
# print('b=',b)
# print('c=',c)
# print('-'*30)
# a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a1)
# # print(a1[2])  #[7 8 9]
# # print(a1[2][1])  #8
# # print(a1[2,1])   #8
# print('a1[:2]\n',a1[:2])
# print('a1[:2,1:]\n',a1[:2,1:])
# print(a1[1,:2])   #[4 5]
# print(a1[2,:1])  #[7]
# print(a1[2,0])  #7
# -------------------------






import numpy as np
# Numerical Python, 과학계산, 데이터 분석시 사용
# print(np.__version__)
# np.info(항목) 도움말
# np.info(np.array)
# 넘파이 배열 생성: 같은 종류의 데이터를 담는 다차원 배열(ndarray)
# 변수 = np.array(list[, 속성])
# li = [1, 2, 3, 4, 5]
# print(li)
# a1 = np.array(li)
# print(a1)
# print(a1.shape) #튜플형태(행수, 열수)
# print(a1.dtype) #데이터 타입
# print(type(a1)) #a1의 타입
# print(a1.ndim) #배열의 차원
# a2 = np.array(li, dtype = np.float64)
# print(a2)
# print(a2.dtype)
# a1 = np.array([1, 2, 3., 4, 5])
# print(a1)

# 2차원
# a2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(a2)
# print(a2.shape)

# 3차원
# a3 = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
# print(a3)
# print(a3.shape)

# 초기화함수
# 변수 = np.zeros(shape, [속성])
# a1 = np.zeros((2, 3))
# print(a1)
# a1 = np.ones((2, 3))
# print(a1)
# a1 = np.full((2, 3), 7)
# print(a1)
# a1 = np.empty((3,4)) #기존 메모리에 남아 있는 값
# print(a1)

# # 단위행렬
# a1 = np.eye(3)
# print(a1)

# li = [[1, 2, 3, 4], [5, 6, 7, 8]]
# print(li)
# a1 = np.ones_like(li)
# print(a1)
# a1 = np.zeros_like(li)
# print(a1)
# # a1 = np.full_like(li, 3.14) #소수점 자름
# a1 = np.full_like(li, 3.54, dtype = np.float64) #소수점까지 출력
# print(a1)
# a1 = np.empty_like(li)
# print(a1)

# 데이터 입출력
# 1. save(파일명, 넘파이배열) binary 형태로 저장
# a0 = np.zeros((4, 3))
# print(a0)
# a1 = np.ones((2, 3))
# print(a1)
# a7 = np.full((5, 2), 7)
# print(a7)
# np.save('data/a0', a0)
# np.save('data/a1', a1)

# # 2. savez(파일명, 넘파이배열1, 넘파이배열2, ...) 두개이상의 ndarray를 binary 형태로 저장
# 여러개 동시 저장시 key가지는 딕셔너리 형태로 저장되어짐
# np.savez('data/all', a0, a1, a7)
# 3. savetxt() text형태로 저장
# 1 변수 = np.load(파일명)
# c0 = np.load('data/a0.npy')
# print(c0)
# c1 = np.load('data/a1.npy')
# print(c1)
# call = np.load('data/all.npz')
# print(call)
# print(call.files) #키값 확인
# print(call['arr_0'])
# print(call['arr_2'])


# 1. 변수 = load()
# 2. 변수 = loadtxt(파일명, 속성)
# data = np.loadtxt('data/d1.txt')
# print(data)

# # 데이터 수직으로 읽기
# data = np.loadtxt('data/d1.txt', unpack = True)
# print(data)
# print(type(data))
# print(data[0]) #data[0] = [1. 2. 3]
# print(data[1])
# print(data[0][0])

# data = np.loadtxt('data/d2.txt', delimiter = ',')
# print(data)
# data = np.loadtxt('data/d2.txt', delimiter = ',', unpack = True)
# print(data)

# data = np.loadtxt('data/d3.txt', delimiter = ',', skiprows = 1)
# print(data)

# 파이썬의 range함수의 넘파이버젼 arange()
# print(np.arange(10))
# print(np.arange(10).astype(np.float)) #데이터형변환

# # 슬라이싱, 색인
# a1 = np.arange(15)
# print(a1)
# print(a1[5])
# print(a1[5:8])
# a1[5:8] = 99
# print(a1)
# print('a1 = ', a1)
# b = a1[5:8]
# print('b = ', b)
# b[1] = 100
# print('b = ', b)
# print('a1 = ', a1)
# # 넘파이에서 배열의 조각은 원본의 뷰
# c = a1[5:8].copy()
# print('c = ', c)
# c[2] = 101
# print('a1 = ', a1)
# print('b = ', b)
# print('c = ', c)

# 슬라이싱 연습
# a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a1)
# print(a1[2]) #[7, 8, 9]
# print(a1[2][1]) #8
# print(a1[2,1]) #8
# print('a1[:2] \n', a1[:2])
# print('a1[:2,1:] \n', a1[:2,1:])
# print('4 5만 출력\n', a1[1, :2])
# print('7 출력\n', a1[2, 0])