import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

print('tips를 읽어서 성별별 식대의 평균, 식대의 중간값, 팁의 합을 출력 agg이용')
data = sb.load_dataset('tips')
data = data.groupby('sex').total_bill.agg(['mean','median','sum'])
print(data)