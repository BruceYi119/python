import os
import pandas as pd
import numpy as np

data = pd.read_csv(os.path.join('data','president.csv'))
data = np.array(data['height'])
print(data.mean())