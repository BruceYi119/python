import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_csv(os.path.join('data','bank.csv'), parse_dates = ['Closing Date','Updated Date'])
data['year'] = data['Closing Date'].dt.year
data['quarter'] = data['Closing Date'].dt.quarter
s1 = data.groupby('year').size()
d2 = s1.reset_index()
d2['new'] = d2['year'].astype(str);
plt.rcParams['figure.figsize'] = (15,10)
plt.plot(d2['new'], d2[0],scalex=20)
plt.title('bank.csv를 읽어 년도별 파산한 은행수를 선그래프로 스타일을 적용하여 이쁘게 작성하세요',size=10)
plt.xlabel('년도')
plt.ylabel('파산은행수')
plt.xticks(size=15,rotation=70)
plt.show()