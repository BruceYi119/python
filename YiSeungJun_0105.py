import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = sb.load_dataset('tips')
print('1)tips데이터를 데이터프레임으로 읽고 식대와 팁과의 관계를 그래프로 표현하세요, 투명도(alpha값을 0.5로 지정)')
data = pd.DataFrame(data)
plt.scatter(data['total_bill'],data['tip'], alpha=0.5)
plt.title('식대와 팁과의 관계')
plt.xlabel('식대')
plt.ylabel('팁')
plt.show()