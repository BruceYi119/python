import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = pd.read_csv(os.path.join('data','gap.tsv'), sep='\t')
data = data[data['continent'] == 'Africa'][['year','country','lifeExp']]
p1 = data[data['country'] == 'Algeria'].pivot('year','country')
p2 = data[data['country'] == 'Angola'].pivot('year','country')
p3 = data[data['country'] == 'Benin'].pivot('year','country')
plt.style.use('bmh')
plt.rcParams['figure.figsize'] = (15,10)
plt.plot(p1, label='Algeria')
plt.plot(p2, label='Angola')
plt.plot(p3, label='Benin')
plt.title('아프리카 대륙의 나라별 기대수명')
plt.xticks(rotation='70', size=11)
plt.xlabel('년도')
plt.ylabel('기대수명')
plt.legend(loc='upper left')
plt.show()