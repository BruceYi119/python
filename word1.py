# https://konlpy.org/ko/latest/
# https://pypi.org/project/wordcloud/#files

import os
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

data = open(os.path.join('data','alice.txt')).read().lower()
sw = STOPWORDS
sw.add('said')
img = Image.open(os.path.join('img','clap.png'))
mask = np.array(img)
wc = WordCloud(max_font_size=100,mask=mask,background_color='white', stopwords=sw).generate(data)
plt.imshow(wc)
plt.axis('off')
plt.show()