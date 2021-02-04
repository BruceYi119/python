import os
import datetime
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='./font/malgun.ttf').get_name()
rc('font',family=fontname)

# data = pd.read_csv(os.path.join('data','ebola.csv'))
# data.info()
#
# now = dt.now()
# print(now)
#
# t1 = now.strftime('%Y-%m-%d')
# t2 = now.strftime('%H:%M:%S')
# print(t1, t2)
#
# t3 = dt(2020,1,1)
# print(t3)

bank = pd.read_csv(os.path.join('data','bank.csv'),parse_dates=['Closing Date','Updated Date'])
bank.info()
bank['year'] = bank['Closing Date'].dt.year
s1 = bank.groupby('year').size()
print(s1)

plt.plot(s1)
plt.xticks(range(2000,2018, 2))
plt.show()