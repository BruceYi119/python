import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = sb.load_dataset('tips')
data['sex2'] = data[['sex']].apply(lambda d: 0 if d['sex'] == 'Female' else 1, axis=1)
fig = plt.figure(figsize=(13, 5))
g1 = fig.add_subplot(2,2,1)
g2 = fig.add_subplot(2,2,2)
g1.hist(data['tip'])
g2.boxplot(data['tip'])
g2.boxplot(data['tip'],vert=False)
fig.suptitle(t='1. 팁의 히스토그램과 상자그림을 하나의 화면에 나타내세요',va='center',ha='center')
fig.tight_layout()
plt.show()