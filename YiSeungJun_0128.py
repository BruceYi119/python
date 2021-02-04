import os
import matplotlib.pyplot as plt
try:
    from cv2 import cv2
except ImportError:
    pass

def mosaic(img,rect,size):                                          #이미지,(시작좌표,끝좌표),축소시킬픽셀
    x1,y1,x2,y2 = rect                                              #시작좌표(x1,y1),끝좌표(x2,y2)
    r = img[y1:y2,x1:x2]
    r = cv2.resize(r,(size,size))                                   #이미지축소
    r = cv2.resize(r,(x2-x1,y2-y1),interpolation=cv2.INTER_AREA)
    #원래크기로 돌리기
    img[y1:y2,x1:x2] = r
    return img

cascadefile = os.path.join('data','f.xml')
cascade = cv2.CascadeClassifier(cascadefile)
img = cv2.imread(os.path.join('img', '2.jpg'))
faces = cascade.detectMultiScale(img, minSize=(150,150))
faces = cascade.detectMultiScale(img, minSize=(30,30))

if len(faces) == 0:
    print('얼굴인식 실패')
    quit()

for (x,y,w,h) in faces:
    img = mosaic(img,(x,y,x + w,y + h), 20)

cv2.imwrite(os.path.join('img','YiSeungJun_0128.jpg'), img)