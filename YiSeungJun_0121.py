import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = sb.load_dataset('tips')
data = data.groupby('smoker').tip.mean()
plt.plot(data)
plt.title('흡연여부별 팁금액의 평균')
plt.xlabel('팁평균')
plt.ylabel('흡연여부')
plt.show()