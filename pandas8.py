import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

# 자료형변환 astype(str)
data = sb.load_dataset('tips')
data['newsex'] = data['sex'].astype(str)

data['total_bill'] = data['total_bill'].astype('str')

data10 = data.head(10)
print(data10)
print(data10.dtypes)

data10.loc[[3,6,9],'total_bill'] = 'not float'
data10['total_bill'] = pd.to_numeric(data10['total_bill'],errors='soerce',downcast='float')
print(data10)

data10['sex'] = data10['sex'].astype(str)
print(data10)
data10['sex'] = data10['sex'].astype('category')

########################################################################################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)
tips=sns.load_dataset('tips')
# print(tips.dtypes)
# 자료형변환(astype(),to_numeric())
tips['newsex']=tips['sex'].astype(str)
# print(tips)
# print(tips.dtypes)
tips['total_bill']=tips['total_bill'].astype(str)
# print(tips)
# print(tips.dtypes)
tips10=tips.head(10)
# print(tips10)
# print(tips10.dtypes)
tips10.loc[[3,6,9],'total_bill']='not float'
# print(tips10)
# tips10['total_bill']=tips10['total_bill'].astype(float)  #err
# print(tips10)
# tips10['total_bill']=pd.to_numeric(tips10['total_bill'])   #err
tips10['total_bill']=pd.to_numeric(tips10['total_bill'],errors='ignore')
print(tips10)
print(tips10.dtypes)   #데이터형 변환X
# tips10['total_bill']=pd.to_numeric(tips10['total_bill'],errors='coerce')
tips10['total_bill']=pd.to_numeric(tips10['total_bill'],
                     errors='coerce',downcast='float')
# print(tips10)
# print(tips10.dtypes)   #데이터형 변환X
# float64는 float32보다 더 많은 범위의 실수를 표현
# tips.info()
# tips['sex']=tips['sex'].astype(str)
# tips.info()
# tips['sex']=tips['sex'].astype('category')
# tips.info()
# 함수---
def double(x):
    print(x,'**')
    return x*2
# print(double(7))
# 시리즈, 데이터프레임에 함수 적용시 apply(함수명)
data=pd.DataFrame({'a':[1,2,3],'b':[10,20,30]})
# print(data)
# s1=data['a'].apply(double)
# print(s1)
# s2=data['b'].apply(double)
# print(s2)
d1=data.apply(double)
print(d1)




print('\n\n\n\n\n\n\n\n\n\n')


def test1(x):
    print(x)
    print('**')
tips10=tips.sample(10,random_state=42)
print(tips10)
# tips10['total_bill'].apply(test1)
# tips10.apply(test1)
print('-'*30)
g1=tips10.groupby('sex')
g1.apply(test1)
print('\n\n\n\n\n\n\n\n\n\n')





import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)
# d1880=pd.read_csv('data/baby/yob1880.txt',names=['name','sex','births'])
# print(d1880)
temp=[]
for year in range(1880,2011):
    filename='data/baby/yob'+str(year)+'.txt'
    # print(filename)
    d1=pd.read_csv(filename,names=['name','sex','births'])
    d1['year']=year
    # print(d1)
    temp.append(d1)   # [1880,1881,...2010]
data=pd.concat(temp,ignore_index=True)
print(data)
# # 년도와 성별에 따른 출생아수
# s1=data.groupby(['year','sex'])['births'].sum()
# print(s1)
# 과제)
# 1.년도, 성별에 따른 출생아수 를 피벗
# 2. 1의 결과를 그래프로   --교통사고 참조
# 3.연도와 이름에 대한 전체 출생수를 피벗


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)
tips=sns.load_dataset('tips')
# print(tips.dtypes)
# # 자료형변환(astype(),to_numeric())
# tips['newsex']=tips['sex'].astype(str)
# # print(tips)
# # print(tips.dtypes)
# tips['total_bill']=tips['total_bill'].astype(str)
# # print(tips)
# # print(tips.dtypes)
# tips10=tips.head(10)
# # print(tips10)
# # print(tips10.dtypes)
# tips10.loc[[3,6,9],'total_bill']='not float'
# # print(tips10)
# # tips10['total_bill']=tips10['total_bill'].astype(float)  #err
# # print(tips10)
# # tips10['total_bill']=pd.to_numeric(tips10['total_bill'])   #err
# tips10['total_bill']=pd.to_numeric(tips10['total_bill'],errors='ignore')
# print(tips10)
# print(tips10.dtypes)   #데이터형 변환X
# # tips10['total_bill']=pd.to_numeric(tips10['total_bill'],errors='coerce')
# tips10['total_bill']=pd.to_numeric(tips10['total_bill'],
#                      errors='coerce',downcast='float')
# print(tips10)
# print(tips10.dtypes)   #데이터형 변환X
# float64는 float32보다 더 많은 범위의 실수를 표현
# tips.info()
# tips['sex']=tips['sex'].astype(str)
# tips.info()
# tips['sex']=tips['sex'].astype('category')
# tips.info()
# 함수---
def double(x):
    print(x,'\n**')
    return x*2
# print(double(7))
# 시리즈, 데이터프레임에 함수 적용시
# 시리즈 또는 데이터프레임.apply(함수명)
# data=pd.DataFrame({'a':[1,2,3],'b':[10,20,30]})
# print(data)
# s1=data['a'].apply(double)
# print(s1)
# s2=data['b'].apply(double)
# print(s2)
# d1=data.apply(double)   #열우선 실행
# print(d1)
# d2=data.apply(double,axis=1)   #행우선 실행
# print(d2)
# def sextonum(x):
#     if x=='Female':
#         return 1
#     else:
#         return 0
# print(tips)
# tips['newsex']=tips['sex'].apply(sextonum)
# print(tips)
def test1(x):
    print(x)
    print('**')
tips10=tips.sample(10,random_state=42)
print(tips10)
# print(test1(77))
# tips10['total_bill'].apply(test1)
# tips10.apply(test1)
print('-'*30)
# g1=tips10.groupby('sex')
# print(g1)
# for g in g1:
#     print(g)
# # g1.apply(test1)
# g2=tips10.groupby(['sex','smoker'])
# g2.apply(test1)
print('-'*30)
# 성별별 식대의 큰금액 2개 추출
def getbill2(x):
    print(x)
    print(x.sort_values(by='total_bill',ascending=False)[:2])
g3=tips10.groupby('sex')
g3.apply(getbill2)


print('\n\n\n\n\n\n\n\n\n\n')








