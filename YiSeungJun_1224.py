import os
import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc

# fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
# rc('font',family=fontname)

# and : &
# or : |

# Serial,INCIDENT TITLE,INCIDENT DATE,LOCATION,DESCRIPTION,CATEGORY,LATITUDE,LONGITUDE,APPROVED,VERIFIED
data = pd.read_csv(os.path.join('data','h.csv'))
print('1) 아이티 지진시 휴대폰으로 응급사항등에 대한 전화내역 파일인 h.csv를 읽어 데이터프레임생성,자료의 행과 열확인,자료형 확인')
print(data.shape, type(data))

print('2)메시지종류(CATEGORY)컬럼 10줄 확인')
print(data['CATEGORY'].head(10))

print('3)CATEGORY가 널인 자료 제거,자료의 행과 열확인')
print(data[data['CATEGORY'].notnull()].shape)

print('4)위치정보가 잘못된 자료 제거,자료의 행과 열확인')
data = data[data['CATEGORY'].notnull()]
print(data[(data['LATITUDE'] > 18) & (data['LATITUDE'] < 20) & (data['LONGITUDE'] > -75) & (data['LONGITUDE'] < -70)].shape)