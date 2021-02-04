import os
import pandas as pd
import seaborn as sns

# movies = pd.read_csv(os.path.join('data','gap.tsv'),header=None,sep = '\t')
# movies = pd.read_csv(os.path.join('data','gap.tsv'),sep = '\t')
# print(movies)

# 샘플데이터
# tips = sns.load_dataset('tips')
# print(tips.tail())
# print(type(tips))

# (행, 열) 정보 (tuple)
# print(tips.shape)

# 컬럼이름
# print(tips.columns)

# 각 열의 데이터 타입
# print(tips.dtypes)

# 정보출력
# tips.info()

# print(tips['total_bill'])
# print(tips['smoker'][0])

# 행접근
# print(tips.loc[200])

# 열접근
# print(tips[['total_bill','tip','sex']])
# print(type(tips[['total_bill','tip','sex']]))

# print(tips.loc[200][['total_bill','tip','sex']])
# print(tips.loc[[1,3,243]][['sex','smoker','size']])

# print(movies.loc[[1700,1702,1703]][['year','continent','country']])

# 열변경
# print(movies[:3])
# m = movies.set_index('lifeExp')
# print(m)
# m = m.reset_index()
# print('-'*30,'\n',m)

# 인덱스 부여
movies = pd.read_csv(os.path.join('data','movie.csv'), header=None)
m = movies.set_index(0)
print(m.iloc[[3,4,5]][1])