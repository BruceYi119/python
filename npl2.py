import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# 단어의 의미는 주변 단어에 의해 형성된다.
# 단어자체는 의미가 없고 그 단어가 사용된 맥락이 의미를 형성
# 통계기반 기법:어떤 주목했을때 그 주변에 어떤 단어가 몇번나오는지 세어 집계하는 방법
# i drink beer
# i guzzle beer
text = 'You say goodbye and I say hello.'
# text = text.lower()
# text = text.replace('.',' .')
# words = text.split(' ')
# print(words)
# word2id = {}  #{you:0,say:1,..}
# id2word = {}  #{0:you,1:say,...}
# for w in words:
#     if w not in word2id:
#         pos=len(word2id)
#         word2id[w]=pos
#         id2word[pos]=w
# print(word2id)
# print(id2word)
# print(word2id['say'])
# print(id2word[3])
# corpus = [word2id[w] for w in words]
# print(corpus)
# corpus = np.array(corpus)
# print(corpus)
def preprocess(text):
    text = text.lower()
    text = text.replace('.',' .')
    words = text.split(' ')
    word2id = {}
    id2word = {}
    for w in words:
        if w not in word2id:
            pos = len(word2id)
            word2id[w] = pos
            id2word[pos] = w
    corpus = np.array([word2id[w] for w in words])
    return corpus, word2id, id2word
corpus, word2id, id2word = preprocess(text)
print(corpus)
print(word2id)
print(id2word)
textlist = ['king is a strong man',
          'queen is a wise woman',
          'boy is a young man',
          'girl is a young woman',
          'prince is a young king',
          'princess is a young queen',
          'man is strong',
          'woman is pretty',
          'prince is a boy will be king',
          'princess is a girl will be queen']
stop_words = ['is', 'a', 'will', 'be']
def delstopword(textlist):
    result = []
    for w in textlist:
        tmp = w.split(' ')
        for stopword in stop_words:
            if stopword in tmp:
                tmp.remove(stopword)
        result.append(' '.join(tmp))
    return result

textlist = delstopword(textlist)
print('textlist =', textlist)
corpus, word2id, id2word = preprocess(' '.join(textlist))
print(corpus)
print(word2id)
print(id2word)
# 윈도우 크기:맥락의 크기(주변단어 몇개 포함여부)를 1로 한경우
#          You say goodbye and I   say  hello .
# you      0    1     0     0  0         0    0
# say      1    0     1     0  1         1    0
# goodbye  0    1     0     1  0         0    0
# and      0    0     1     0  1         0    0
# i        0    1     0     1  0         0    0
# hello    0    1     0     0  0         0    1
# .        0    0     0     0  0         1    0
c = np.array([
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0]
])
# print(c)
# print(id2word[0],'==>를 벡터로 ',c[0])
# print(id2word[4],c[4])
# print(c[word2id['goodbye']])
def corpus2matrix(corpus, wordsize, windowsize = 1):
    result = np.zeros((wordsize,wordsize))
    # print(result)
    for idx, wid in enumerate(corpus):
        print('idx,wid=', idx, wid)
        for i in range(1, windowsize + 1):
            leftidx = idx - i
            rightidx = idx + i
            if leftidx >= 0:
                leftwordid = corpus[leftidx]
                result[wid, leftwordid] += 1

    return result

c = corpus2matrix(corpus, 7)
print(c)
# 벡터사이의 유사도-코사인유사도(-1~1 사이의 값), 유클리드 거리등
def cos_similarity(x, y):
    nx = x / np.sqrt(np.sum(x ** 2))
    ny = y / np.sqrt(np.sum(y ** 2))
    return  np.dot(nx, ny)
print('you와 i의 유사도 =', cos_similarity(c[word2id['you']], c[word2id['i']]))
# ------------------------
x=np.array([100,-5,2])
print('x=',x)
print('x.argsort()=',x.argsort())   #오름차순정렬하여 배열의 인덱스 반환
print('(-x).argsort()=',(-x).argsort())  #내림차순 정렬
# you단어와 유사한 단어 5개 출력
def rank_similar(word,word2id,id2word,c,top=5):
    # print('word=',word)
    # print('wordid=',word2id[word])
    # print('wordvec=',c[word2id[word]])
    sim=np.zeros(len(id2word))
    for i in range(len(id2word)):
        sim[i]=cos_similarity(c[i],c[word2id[word]])
    print('sim=',sim)
    print('내림차순 argsort()=',(-1*sim).argsort())
    cnt=0
    for i in (-1*sim).argsort():   #[0 2 4 5 1 3 6]
        if id2word[i]==word:
            continue
        print('{},{}'.format(id2word[i],sim[i]))
        cnt=cnt+1
        if cnt>=top:
            return
rank_similar('you',word2id,id2word,c)