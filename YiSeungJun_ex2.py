import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_csv(os.path.join('data','alcol.csv'))

print('1)미국의 주별 1인당 알코올 소비데이터인 alcol.csv 파일을 State가 인덱스인 data라는 데이터프레임으로 생성한후 처음 5개의 데이터를 출력하세요')
print(data.set_index('State').head(5))

print('2)년도를 행인덱스 주를 열이름으로 하여 와인소비량을 나타내는 피벗테이블 data_wine을 생성후 확인하세요')
data_wine = pd.pivot_table(data, index='Year', columns='State', values='Wine', aggfunc=sum)
print(data_wine)

print('3)2009년 데이터만 따로 하여 data2009라는 데이터프레임으로 생성하고 데이터의 행 과 열을 확인하세요')
data2009 = data[data['Year'] == 2009]
print(data2009.shape)

print('4)data2009에서 Year열을 삭제하고 인덱스를 0부터 시작하는 일련번호로 재설정하세요')
data2009 = data2009.drop(['Year'], axis='columns')
data2009 = data2009.reset_index(drop=True)
print(data2009)

print('5)data2009에서 각각 열의 누락값의 갯수를 확인하고 0으로 누락값을 교체하세요')
data2009 = data2009.fillna(0)
print(data2009)

print('6)data2009에 \'Beer\',\'Wine\',\'Spirits\'열의 합인 total 열을 추가하세요')
data2009['total'] = data2009[['Beer','Wine','Spirits']].apply(lambda d: d['Beer']+d['Wine']+d['Spirits'], axis=1)
print(data2009)

print('7)미국인구통계데이터를 읽어 usa 데이터프레임 생성하고 \'미국\'라는 값을 가지는 country열을 추가하세요')
usa = pd.read_csv(os.path.join('data','usa.csv'))
usa['country'] = '미국'
print(usa)

print('8)data2009와 usa 데이터 프레임을 합쳐서 df라는 데이터프레임으로 생성하고 인덱스 를 State로 지정하세요')
df = pd.concat([data2009, usa], axis=1)
df.columns = ['State', 'Beer', 'Wine', 'Spirits', 'total', 'rState', 'Population', 'country']
df = df.drop(['rState'], axis='columns')
print(df)

print('9) 캐나다 인구데이터를 가지고 있는 canada.csv를 읽어 canada라는 데이터프레임으로 생성하고 \'캐나다\'라는 값을 가지는 country열을 추가하세요')
canada = pd.read_csv(os.path.join('data','canada.csv'))
canada['country'] = '캐나다'
print(canada)

print('10) usa 와 canada 데이터프레임을 합쳐서 pop라는 데이터 프레임으로 생성하고 country와 state를 인덱스로 지정한 후 데이터를 인덱스 순서로 정렬하여 확인하세요')
pop = pd.concat([usa, canada], axis=0)
pop = pop.set_index(['country','State'])
print(pop)