import numpy as np
# a1=np.array([[1,2,3],[4,5.,6]])
# print(a1)
# a2=np.ones((2,4,2))
# print(a2)
# 데이터 생성
# np.linspace(start,stop,개수[,속성])
# a3=np.linspace(0,1,5)
# start<=data<=stop
# print(a3)
# a3=np.linspace(0,1,5,endpoint=False)  #endpoint:stop값 포함여부
# start<=data<stop
# print(a3)
# np.arange(시작,종료,증감)   #파이썬의 range함수
# a3=np.arange(10,20,2)
# print(a3)
# a3=a3.astype(np.float)
# print(a3)
# a3=np.arange(10) #0부터 시작하고 증감값이 1인경우 종료값만 지정
# print(a3)
# a3=np.arange(0,10,3)
# print(a3)
# 난수생성
# 변수=np.random.randint(low,high,속성)
# low<=data<high 난수를 정수로 발생
# a3=np.random.randint(1,10,size=(10,))
# print(a3)
# a3=np.random.randint(1,100,size=(2,3))
# print(a3)
# a3=np.random.randint(100,size=(2,3))   #low값이 0인경우
# print(a3)
# # seed값 : 난수발생위치를 고정
# seed에서 사용하는 숫자는 난수발생위치를 지정하는것으로 무엇이든 상관X
# np.random.seed(1)
# a3=np.random.randint(10,size=(2,3))   #low값이 0인경우
# print(a3)
# a3=np.random.randint(100,size=(2,3))   #low값이 0인경우
# print(a3)
# 변수=np.random.normal([속성])
# 정규분포에서 표본추출한 난수를 발생
# 속성 loc :정규분포의 평균, default 0
#      scale:표준편차,  default 1
#      size:shape
# a3=np.random.normal(loc=0,scale=1,size=(1000,))
# print(a3)
# import matplotlib.pyplot as plt
# plt.hist(a3)
# plt.show()
# np.random.rand(행수,열수)  :0-1사이의 균등분포형상으로 난수
# np.random.randn(행수,열수) :가우시안표준정규분포
# np.random.random([size]) :0-1 균등분포형상으로 난수
# a3=np.random.rand(3,2)
# print(a3)
# a3=np.random.randn(10)
# print(a3)
# a3=np.random.randn(2,4)
# print(a3)
# a3=np.random.random(size=(2,4))
# print(a3)
# print('-'*30)
# 파일입출력
# a1=np.random.randint(0,10,size=(2,4))
# print(a1)
# # text형태로 저장 및 불러오기
# # np.savetxt(파일명,배열,옵션)
# # np.savetxt('data\\a1.csv',a1)
# # np.savetxt('data\\a1.csv',a1,delimiter=',')
# # np.loadtxt(파일명,옵션)
# # b1=np.loadtxt('data\\a1.csv',delimiter=',')
# # b1=np.loadtxt('data\\a1.csv',delimiter=',',dtype=np.int)
# # print(b1)
# #binary 형태의 저장및 불러오기
# # np.save(파일명,배열명)
# # np.savez(파일명,배열명1,배열명2,..)
# # 배열 여러개를 저장시키면 딕션어리 형태로 저장
# # np.savez(파일명,key1=배열명1,key2=배열명2,..)
# # np.load(파일명)
# a2=np.ones((10,))
# print(a2)
# np.save('data\\aa1',a1)
# np.savez('data\\aa2',a1,a2)
# np.savez('data\\aa3',a1=a1,a2=a2)
# print('-'*30)
# c1=np.load('data\\aa1.npy')
# c2=np.load('data\\aa2.npz')
# c3=np.load('data\\aa3.npz')
# print(c1)
# print(c2)
# print(c3)
# print('npz파일의 키값 확인',c2.files)
# print(c2['arr_0'])
# print(c2['arr_1'])
# print('npz파일의 키값 확인',c3.files)
# print(c3['a1'])
# print(c3['a2'])
# li=[3.56,10.1,3,5,7]
# a1=np.array(li)
# print(a1)
# a1=np.array(li,dtype=np.int)
# print(a1)
# a1=np.array(li,dtype=np.string_)
# print(a1)
# 연산
# a1=np.array([[1,2,3],[4,5,6]],np.float)
# print(a1)
# print(a1+a1)
# print(a1-a1)
# print(1/a1)
# 불린추출
# np.random.seed(10)
# names=np.array(['kim','park','lee','kim','lee','park','park'])
# print(names)
# score=np.random.randint(0,100,(7,3))
# # 각 이름이 score의 행에 대응된다고 가정
# print(score)
# print(names=='kim') #[ True False False  True False False False]
# print(score[names=='kim'])
# print(score[names=='kim',2:])
# print(score[names=='kim',1:])
# print('-'*30)
# print(score[names=='kim',2])
# print('-'*30)
# print(score[names!='kim'])
# print(score[~(names=='kim')])
# print('-'*30)
# print(score[(names=='park')|(names=='lee')])
# and,or 사용X, &,| 사용
# 점수가 30미만은 0으로
# print(score[score<30])
# score[score<30]=0
# print(score)
# 2014년 시애틀의 1월 강수량(PRCP)의 평균
# import pandas as pd
# data=pd.read_csv('data\\seattle.csv')
# print(data)
# rain=data['PRCP']
# print(비)
# days=np.arange(365)
# print(days)
# chk=days<=30
# print(chk)
# jan=rain[chk]   #1월강수량
# print(jan)
# print(np.mean(jan))
#-------------------
# a1=np.arange(15)
# print(a1)
# a1=a1.reshape((3,5))
# print(a1)
# # a1=a1.reshape((3,6))  err  데이터갯수 동일
# # print(a1)
# # a1=a1.reshape((3,3))
# # print(a1)
# #--------------
# a2=np.arange(15)
# print(a2)
# a2=np.resize(a2,(3,5))
# print(a2)
# a2=np.resize(a2,(3,3))
# print(a2)
# a2=np.resize(a2,(3,8))
# print(a2)
# a1=np.array(np.arange(16))
# print(a1)
# a1=np.arange(16)
# print(a1)
# a1=a1.reshape(2,4,2)
# print(a1)
# a1=a1.reshape(-1,4)
# # a1=a1.reshape(4,4)
# print(a1)
# a1=a1.reshape(-1,2,2)
# print(a1)
# a1=a1.reshape(-1)
# print(a1)
# --------------------
# 행렬곱
# (2,3)X(3,5) =(2,5)
a=np.array([[1,2,3],[4,5,6]])   #(2,3)
b=np.array([[1,0,-1],[1,1,0]])  #(2,3)
print(a)
print(b)
# print(np.dot(a,b))   #행렬곱
# (2,3)X(2,3) =err
# 전치행렬
print('-'*30)
print(b.T)    #(3,2)
print(np.dot(a,b.T))
#(2,3)X(3,2)=(2,2)
# 과제
# 미국대통령의 키를 저장한 파일을 읽고 키의 평균을 구하세요








# 프젝팀?