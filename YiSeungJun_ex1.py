import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_csv(os.path.join('data','rtest.csv'))
print('1) data 데이터 프레임의 각 열의 데이터 타입과 행과 열의 수를 확인하시오')
print(data.shape)

def convertResident(v):
    resident = { 1: '서울', 2: '인천', 3: '대전', 4: '대구', 5: '시구군' }
    return resident.get(v);

print('2) 거주지(regident) 컬럼은 다음과 같다. regident2컬럼을 추가하여 해당하는 지역을 표현하시오 1. 서울 2. 인천 3. 대전 4. 대구 5.시구군')
data['resident2'] = data['resident'].apply(convertResident)
print(data['resident2'])

print('3) age변수가 널인 자료 제거하고 자료의 행과 열의 수를 확인하시오')
print(data[data['age'].notnull()].shape)

print('4) age변수의 최소값, 최대값, 평균을 출력하시오.')
print(data['age'].min(), data['age'].max())

print('5) age 변수를 박스그림으로 표현하여 값의 범위를 확인하시오')
# plt.boxplot(data.groupby('age')['age'].size(), labels=['갯수'])
# plt.title('age 박스그림')
# plt.ylabel('나이 범위')
# plt.show()

def convertAge(v):
    if v < 30:
        return '청년층'
    elif (v >= 31) & (v < 56):
        return '중년층'
    else:
        return '장년층'

print('6) age 변수를 참조하여 30세이하는 청년층, 31세-55세는 중년층,56세 이상은 장년층으로 하여 age2변수를 추가하시오')
data['age2'] = data['age'].apply(convertAge)
print(data['age2'])

def converGender(v):
    if v == 1:
        return '남자'
    else:
        return '여자'

print('7) data의 gender 칼럼을 대상으로 1->"남자", 2->"여자" 형태로 코딩 변경하여 gender2')
data['gender2'] = data['gender'].apply(converGender)
print(data['gender2'])

print('8) gender2칼럼을 기준으로 남녀의 빈도수를 확인하시오')
data1 = data.groupby('gender').gender.sum()
data1.index = ['남자','여자']
print(data1)

print('9) 7번의 결과를 파이차트로 표현하시오')
# plt.pie(data1.values,labels=data1.index,colors=['blue','orange'],autopct='%.2f%%')
# plt.title('남자/여자 빈도수')
# plt.xlabel('')
# plt.ylabel('')
# plt.show()

print('10) 나이에 따른 구매비용의 관계를 그래프로 표현하시오')
# plt.scatter(data['age'],data['price'])
# plt.title('나이에 따른 구매비용 산점도')
# plt.xlabel('나이')
# plt.ylabel('구매비용')
# plt.show()