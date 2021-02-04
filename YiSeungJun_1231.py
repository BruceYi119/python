import os
import pandas as pd
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

print('1) 아이티 지진시 휴대폰으로 응급사항등에 대한 전화내역 파일인')
data = pd.read_csv(os.path.join('data','h.csv'))
print(data)

print('2)CATEGORY가 널인 자료 제거')
data = data[data['CATEGORY'].notnull()]
print(data)

print('3)CATEGORY 열을  코드번호, 코드명으로 분리하세요')
data['CODE'] = data[['CATEGORY']].apply(lambda d: d['CATEGORY'].split(',')[0], axis=1)
data['CODENAME'] = data[['CATEGORY']].apply(lambda d: d['CATEGORY'].split(',')[1], axis=1)
print(data[['CODE','CODENAME']])