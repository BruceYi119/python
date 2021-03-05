# pip install gensim
# import re
# from gensim.models.word2vec import Word2Vec
# data=open('data\\grim.txt',encoding='utf-8').read()
# # print(data)
# # print(data[2674:530000])
# text=data[2674:530000]
# text=re.sub(r'[^a-zA-Z\.]',' ',text)
# # import nltk
# # from nltk.tokenize import word_tokenize
# # from nltk.corpus import stopwords
#
# sen=text.split('.')   #문장단위로 자르기
# words=[s.split(' ') for s in sen]
# print(words)    #[[단어1,단어2,..],[],[]...]
#
# model=Word2Vec(words,sg=1,size=100,window=3,min_count=3)
# # #  # sg 알고리즘 선택    0:CBOW,   1:skip gram
# # #  # size
# # #  # min_count 사용할 단어의 최소빈도
# model.save('data\\grim.model')
# # ------
# model=Word2Vec.load('data\\grim.model')
# print('princess단어를 벡터로',model.wv['princess'])
# print('princess단어를 벡터로',model.wv['princess'].shape)
# print('유사도',model.similarity('princess','queen'))
# print('1번)가장 유사한 단어',model.most_similar('princess'))
# print('2번)가장 유사한 단어3개 추출',model.most_similar('princess',topn=3))
# print('3번)가장 유사한 단어',model.most_similar(positive=['princess']))
# # princess+man-woman
# print('4번)가장 유사한 단어',model.most_similar(positive=['princess','man'],
#                         negative=['woman']))
# --------------------------------
from konlpy.tag import Okt
from gensim.models.word2vec import Word2Vec,Text8Corpus
with open('data\\news.csv',encoding='utf-8')  as f:
    text=f.read()
lines=text.split('\n')
okt=Okt()
result=[]
for line in lines:
    mallist=okt.pos(line,norm=True,stem=True)
    # print(mallist)  #[('지난해', 'Noun'), ('글로벌', 'Noun'),...]
    temp=[]
    for word in mallist:  #word=('지난해', 'Noun'),('글로벌', 'Noun')
        if not word[1] in ['Alpha','Punctuation','Josa','Number','Eomi','Foreign']:
            temp.append(word[0])
    # print(temp)  #['지난해', '글로벌', '관련'..]
    result.append(' '.join(temp))
# print(result)
data=' '.join(result)
# print(data)   #공백으로 구분








