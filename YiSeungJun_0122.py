import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

data = sb.load_dataset('tips')
data = data[['sex','total_bill','day']]
data = data.pivot_table(data, index=['sex','day'], aggfunc=sum)
sb.lineplot(data=data, x='day', y='total_bill', hue='sex')
plt.title('tips데이터를 활용하여 성별 요일별 식대의 합을 출력하세요(피벗테이블 이용하세요)')
plt.xlabel('성별 요일별')
plt.ylabel('식대의 합')
plt.show()