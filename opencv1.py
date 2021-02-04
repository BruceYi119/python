# pip install opencv-python
import os
try:
    from cv2 import cv2
except ImportError:
    pass
import matplotlib.pyplot as plt
# img=cv2.imread('img\\g.jpg')  #이미지 읽기
# print(img)
# print(type(img))   #넘파이배열
# plt.imshow(img)  #이미지출력
# matplotlib의 색순서는 RGB  ff0000
# opencv 의 색순서는 BGR
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.axis('off')  #축제거
# plt.show()
# cv2.imwrite('img\\g2.png',img)   #이미지저장
# 이미지 크기변경
# img2=cv2.resize(img,(500,300))
# cv2.imwrite('img\\g3.png',img2)
# plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
# plt.show()
# 이미지자르기
# img3=img[400:600,250:400]
# img3=cv2.resize(img3,(300,300))
# plt.imshow(cv2.cvtColor(img3,cv2.COLOR_BGR2RGB))
# plt.show()
# -----------------
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# 캐스케이드파일:얼굴데이터베이스
# cascadefile='f.xml'
# cascade=cv2.CascadeClassifier(cascadefile)
# # img=cv2.imread('img\\g.jpg')
# img=cv2.imread('img\\2pm.jpg')
# # 그레이스케일로 변환:이미지 내부의 명암을 기반으로 얼굴인식
# img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 얼굴인식
# faces=cascade.detectMultiScale(img2,minSize=(150,150))
# minSize 얼굴인식의 최소크기지정
# faces=cascade.detectMultiScale(img2,minSize=(30,30))
# print(type(faces))  #넘파이배열
# print(len(faces))  #인식한 얼굴갯수
# if len(faces)==0:
#     print('얼굴인식 실패')
#     quit()
# print(faces)
# # 얼굴인식부분 표시
# for (x,y,w,h) in faces:
#     print('얼굴좌표=',x,y,w,h)
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=5)
#                  #이미지,시작좌표,끝좌표,색상, 선두께
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.show()
# ------모자이크처리
def mosaic(img,rect,size):    #이미지,(시작좌표,끝좌표),축소시킬픽셀
    x1,y1,x2,y2=rect  #시작좌표(x1,y1),끝좌표(x2,y2)
    r1=img[y1:y2,x1:x2]
    r1=cv2.resize(r1,(size,size))   #이미지축소
    r1=cv2.resize(r1,(x2-x1,y2-y1),interpolation=cv2.INTER_AREA)
    #원래크기로 돌리기
    img[y1:y2,x1:x2]=r1
    return img

img=cv2.imread('img\\dog.jpg')
newimg=mosaic(img,(50,50,200,200),20)
plt.imshow(cv2.cvtColor(newimg,cv2.COLOR_BGR2RGB))
plt.show()

# 과제
# 사람의 얼굴을 인식한후 얼굴부분 모자이크 처리하여 이미지를 저장하세요
# 소스와 이미지 제출