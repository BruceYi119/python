import os
import numpy as np

data = np.loadtxt(os.path.join('data','water.csv') ,delimiter=',', skiprows=1, dtype='int')
print('x\n', data[range(len(data)),:2])
print('y\n', data[range(len(data)),2:3])