import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = sb.load_dataset('tips')
data = data.groupby('day').total_bill.sum()
print(data)
plt.plot(data)
plt.title('요일별 식대의 합')
plt.xlabel('요일')
plt.ylabel('식대')
plt.show()