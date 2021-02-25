import os
import pandas as pd
import seaborn as sb
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

print('1) 데이터 시각화의 개념과 목적을 쓰시오.')
print('데이터 시각화는 많은 데이터를 한눈에 보기 쉽게 표 또는 그래프 등등으로 시각적으로 표현하는것입니다')

data = pd.read_csv(os.path.join('data','report.csv'))
print('2)report.csv파일을 활용하여 데이터를 데이터프레임으로 읽어 들여 해당 데이터프레임의 변수들을 확인하고 처음 10개, 마지막 10개의 데이터를 출력하시오')
data.info()
print(data.head(10))
print(data.tail(10))

print('3) report.csv파일을 활용하여 New Hampshire주의 Beer 소비량과 Wine 소비량의 산점도를 나타내시오')
# sb.scatterplot(data=data , x='Beer', y='Wine', hue='Year')
# plt.title('Beer 소비량과 Wine 소비량의 산점도')
# plt.xlabel('맥주')
# plt.ylabel('와인')
# plt.show()

print('4)report.csv파일을 활용하여 New Hampshire, Colorado, Utah 주의 맥주 소비량의 변화를 선그래프로 작성하시오 (그래프제목 : 주별 맥주 소비량의 변화, 범례추가, x축제목 : 년도, y축제목 : 맥주소비량, 스타일 :ggplot)')
# data = data[(data['State'] == 'New Hampshire') | (data['State'] == 'Colorado') | (data['State'] == 'Utah')][['State','Year','Beer']];
# sb.lineplot(data=data, x='Year', y='Beer', hue='State')
# plt.title('주별 맥주 소비량의 변화')
# plt.xlabel('년도')
# plt.ylabel('맥주소비량')
# plt.show()

print('5)tips 데이터의 각 열의 데이터 형을 확인하시오')
tips = sb.load_dataset('tips')
tips.info()

print('6)tips 데이터에서 식사시간별 total_bill의 최소값, 최대값, 평균, 중간값을 확인하고 상자그림을 그리시오')
print(tips.groupby('time').total_bill.agg(['min','max','mean','median']))
# sb.boxplot(x="time", y="total_bill", data=tips, hue="time")
# plt.legend(loc='upper center')
# plt.show()

print('7)tips 데이터에서 행인덱스로 좌석수, 열인덱스로 요일을 지정하여 식사비용의 금액의 합계를 나타내시오')
data = tips[['day','size','total_bill']].pivot_table(tips[['day','size','total_bill']], index=['day','size'] , aggfunc=sum)
print(data)

print('8) 7번의 결과를 선그래프로 나타내시오.')
# sb.lineplot(data=data, x="size", y="total_bill", hue='day')
# plt.title('식사 비용 현황')
# plt.xlabel('좌석수')
# plt.ylabel('식사비용')
# plt.show()

print('9) bank.csv 데이터 파일의 데이터를 확인하고 날짜와 관련된 열은 datetime형으로 변환하시오')
data = pd.read_csv(os.path.join('data','bank.csv'), parse_dates = ['Closing Date','Updated Date'])
print(data)

print('10) bank.csv 데이터에서 연도별 파산한 은행의 수를 그래프로 표시하시오')
data['Year'] = data['Closing Date'].dt.year
data = data.groupby('Year').count()
sb.lineplot(data=data, x='Year', y='Bank Name')
plt.title('연도별 파산한 은행의 수')
plt.xlabel('년도')
plt.ylabel('파산은행수')
plt.show()