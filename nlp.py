# NLP : 우리의 말을 컴퓨터에게 이해시키기 위한 분야
# 말의 의미는 단어로 구성
# 컴퓨터에게 단어의 의미를 이해시키기
# 1) 시소러스(유의어 사전):사람이 직접 단어의 의미를 정의, 뜻이 같은 단어나 뜻이 비슷한 단어를 그룹으로 분류
# 2) 통계기반
# 3) 추론기반

import os
import re
import nltk                                             # National Language Tollkit
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# nltk.download('wordnet')
# print(wordnet.synsets('car'))
# c1 = wordnet.synset('car.n.01')
# print('컴퓨터가 아닌 사람이 이해하는 내용', c1.definition())
# print('동의어 그룹에 속한 단어들', c1.lemma_names())
# print('상위어', c1.hypernyms())
# print('상위어경로', c1.hypernym_paths())
# print('하위어', c1.hyponyms())
# e1 = wordnet.synset('entity.n.01')
# print(e1.definition())
# print(e1.lemma_names())
# print(wordnet.synsets('book'))
# b1 = wordnet.synset('book.n.01')
# d1 = wordnet.synset('dog.n.01')
# print(b1.hypernym_paths())
# print(d1.hypernym_paths())
# 유사도(0-1의 값)
# print('책과 자동차의 유사도', b1.path_similarity(c1))
# print('책과 강아지의 유사도', b1.path_similarity(d1))
# cat = wordnet.synset('cat.n.01')
# print('고양이와 강아지의 유사도', cat.path_similarity(d1))
# print('고양이와 자동차의 유사도', cat.path_similarity(c1))
# 정규화
# 1) 토큰화 : 문자열을 여러개의 조각으로 나눔. 문장토큰아니저, 단어토큰나이저
# 2) 단어의 대소문자 통일
# 3) 불용어 제거(stopwords)
# 4) 원형추출
# 5) 품사태깅
# str = 'This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or'
# words = word_tokenize(str)
# words = [w.lower() for w in words]
# str = 'This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or'.lower()
# words = word_tokenize(str)          # 단어단위
# words2 = sent_tokenize(str)         # 문장단위
# print(len(words))
# print(stopwords.words('english'))
# 불용어 제거
# stopwords = stopwords.words('english')
# words = [w for w in words if w not in stopwords]
# print(len(words))
# 원형추출
# lem = nltk.WordNetLemmatizer()
# print('원형추출 =', lem.lemmatize('girls'))
# print('원형추출 =', lem.lemmatize('boies'))
# words = [lem.lemmatize(w) for w in words]
# print('원형추출후 =', words)
# 품사태깅
# nltk.download('averaged_perceptron_tagger')
# print(nltk.pos_tag(['pretty','girl']))

# text = open(os.path.join('data','alice.txt')).read()
# text = text.lower()
# words = nltk.tokenize.word_tokenize(text)
# print('단어단위 갯수 =',len(words))
# words = [w for w in words if w not in stopwords.words('english') and w.isalnum()]
# print('불용어 제거 후 단어단위 갯수 =', len(words))
# words[0] = words[0].replace('癤풮', 'P')
# lem = nltk.WordNetLemmatizer()
# print(words)
# words = [lem.lemmatize(w) for w in words]
# print(words)
# with open(os.path.join('data','alice2.txt'), 'w') as f:
#     f.write(' '.join(words))

# data = open(os.path.join('data', 'alice2.txt')).read()
# img = Image.open(os.path.join('img','wine.png'))
# mask = np.array(img)
# for i in range(len(mask)):
#     for j in range(len(mask[i])):
#         if mask[i][j] == 0:
#             mask[i][j] = 255
# wc = WordCloud(background_color='white', max_words=2000, mask=mask).generate(data)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()

# 통계기반 기법
def preprocess(text):
    text = re.sub(r'\.', '', text.lower())
    words = text.split(' ')
    words = [w for w in words if w not in stopwords.words('english') and w.isalnum()]
    wordToId = {}   # { 0: 'say', 1: 'happy' }
    idToWord = {}
    for w in words:
        if w not in wordToId:
            wordToId[w] = len(wordToId)
            idToWord[len(wordToId) - 1] = w
    corpus = [wordToId[w] for w in words]
    corpus = np.array(corpus)
    return wordToId, idToWord, corpus

text = open(os.path.join('data','alice2.txt')).read()

wordToId, idToWord, corpus = preprocess(text)
data = ' '.join(list(wordToId.keys()))
img = Image.open(os.path.join('img','wine.png'))
mask = np.array(img)
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] == 0:
            mask[i][j] = 255
wc = WordCloud(background_color='white', max_words=2000, mask=mask).generate(data)
plt.imshow(wc)
plt.axis('off')
plt.show()

# 맥락 : (주목하는 단어) 주변에 놓인 단어
# 통계기반기법 : 어떤 단어에 주목했을때 그 주변에 어떤 단어가 몇번 나오는지 세어서 집계
# 윈도우 크기를 1로 한 경우
#                You say goodbye and i say hello .
#                 0   1     2     3  4  1    5
# you :           0   1     0     0  0  0    0
# say :           1   0     1     0  1  0    1
# goodbye :       0   1     0     1  0  0    0