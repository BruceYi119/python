import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

print('1)tips데이터를 이용하여 요일을 행인덱스, 성별을 열인덱스로 하여 식사금액의 합을 출력하세요')
data = sb.load_dataset('tips')
data = data[['total_bill','day','sex']]
data = data.groupby(['day','sex']).total_bill.sum()
print(data)