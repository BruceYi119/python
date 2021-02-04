import os
import pandas as pd
import seaborn as sb
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_csv(os.path.join('data','accident.csv'))
# 1)요일별교통사고사망자수의합계를출럭하고선그래프로출력하시오
d1 = data[['요일','사망자수','발생년']]
# sb.lineplot(data=d1, x='요일', y='사망자수', hue='발생년')
# plt.show()

# 2)2014년서울지역의구별교통사고사상자수의합을출력하고그래프로표현하시오
d2 = data[(data['발생년'] == 2014) & (data['발생지시도'] == '서울')]
print(d2.groupby('발생지시군구')['사상자수'].sum())
# sb.countplot(data=d2, x='발생지시군구', hue='발생년')
# plt.ylabel('사상자수')
# plt.show()

# 3)년도별발생지시도별교통사고사망자수의합을확인하고그래프로시각화하시오
d3 = data[['발생년','발생지시도','사망자수']]
# sb.countplot(data=d3, x='발생지시도', hue='발생년')
# plt.ylabel('사망자수')
# plt.show()

# 4-9)ebola데이터를활용하여다음을진행하시오.
data = pd.read_csv(os.path.join('data','ebola.csv'))
# 4)ebola의행과열,그리고각열의데이터타입을확인하시오.
data.info()

# 5)Date열의자료형을datetime형으로변환하시오
def convertDate(v):
    d = v.split('/')
    return dt.date(int(d[2]), int(d[0]), int(d[1]))

data['Date'] = data['Date'].apply(convertDate, convert_dtype=dt.date)
print(data)

# 6)Date열을참고하여년,월,일열을추가하시오
data['year'] = data['Date'].apply(lambda d : d.year)
data['month'] = data['Date'].apply(lambda d : d.month)
data['day'] = data['Date'].apply(lambda d : d.day)
print(data)

# 7)에볼라최초발생일을출력하시오
print(min(data['Date']))

# 8)Date열을인덱스로지정하시오.(이때누락된일자가없도록날짜범위를생성)
pd.date_range(start='2014-03-22',end='2015-01-05')
data = pd.read_csv(os.path.join('data','ebola.csv'), index_col='Date')
print(data)

# 9)일자별사망자수를선그래프로출력하시오
data = pd.read_csv(os.path.join('data','ebola.csv'))
data['Date'] = data['Date'].apply(convertDate, convert_dtype=dt.date)
# sb.lineplot(data=data, x='Date', y='Deaths_Guinea')
# sb.lineplot(data=data, x='Date', y='Deaths_Guinea')
# sb.lineplot(data=data, x='Date', y='Deaths_Liberia')
# sb.lineplot(data=data, x='Date', y='Deaths_SierraLeone')
# sb.lineplot(data=data, x='Date', y='Deaths_Senegal')
# sb.lineplot(data=data, x='Date', y='Deaths_UnitedStates')
# sb.lineplot(data=data, x='Date', y='Deaths_Spain')
# sb.lineplot(data=data, x='Date', y='Deaths_Mali')
# plt.ylabel('사망자수')
# plt.legend(['Guinea','Liberia','SierraLeone','Senegal','UnitedStates','Spain','Mali'])
# plt.show()

# 10)판다스에서데이터유형을비교하시오
# 1) 비교 연산자( ==, >, >=, <, <=, != )
# 2) in 연산자( in, ==, not in, != )
# 3) 논리 연산자(and, or, not)
# 4) 외부 변수(또는 함수) 참조 연산
# 5) 인덱스 검색
# 6) 문자열 부분검색( str.contains, str.startswith, str.endswith )