import os
import pandas as pd
import seaborn as sb

data = sb.load_dataset('tips')
data.to_csv(os.path.join('data','tips.csv'), index=False)