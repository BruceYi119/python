import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

def age(v):
    if (v >= 1) & (v < 18):
        return 'Under 18'
    elif (v >= 18) & (v < 25):
        return '18-24'
    elif (v >= 25) & (v < 35):
        return '25-34'
    elif (v >= 35) & (v < 45):
        return '35-44'
    elif (v >= 45) & (v < 50):
        return '45-49'
    elif (v >= 50) & (v < 56):
        return '50-55'
    else:
        return '56+'

def getMinRating(d):
    print(d.sort_values(by='Rating',ascending=True)[:3])

data = pd.read_csv(os.path.join('data','movie_rating_user.csv'))
data['Newage'] = data['Age'].apply(age)
print('1)data 데이터프레임의 \'Age\'열을 활용하여 data[\'Newage\']열을 생성하세요')
print(data)

print('2) 연령대별 평점점수의 평균 출력(data[\'Newage\']열 활용)')
data1 = data.groupby('Newage').Rating.mean()
print(data1)

print('3) 연령대별 평점점수가 낮은 사람 3건 출력(data[\'Newage\']열 활용)')
data2 = data.groupby('Newage')[['Newage','UserID','Rating','Age']]
data2.apply(getMinRating)