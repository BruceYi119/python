from konlpy.tag import Okt
# 많이 사용된 명사 30개 추출
# {'꽃':10,'컴퓨터':2,...}
# data=open('data\\news.csv',encoding='utf-8').read()
# lines=data.split('\n')
# okt = Okt()
# maldic={}
# for line in lines:
#     # malist=okt.pos(line)
#     malist=okt.nouns(line)
#     # print(malist)
#     for mal in malist:
#         if mal not in maldic:
#             maldic[mal]=0
#         maldic[mal]=maldic[mal]+1
#     # break
# print(maldic)
# print(sorted(maldic))
# print(sorted(maldic.items(),reverse=True))
# nlist=sorted(maldic.items(),key=lambda x:x[1],reverse=True)
# print(nlist)
# print(nlist[:30])
# for n in nlist[:30]:
#     print(n[0], end=' ')
#  코로나와 가장 유사한 단어 3개 출력 ----------------------
# data=open('data\\news.csv',encoding='utf-8').read()
# fw=open('data\\news2.csv','a',encoding='utf-8')   #단어 단어 단어
# lines=data.split('\n')
# okt = Okt()
# maldic={}
# for line in lines:
#     malist=okt.pos(line)
#     print(malist)
#     templist=[]
#     for mal in malist:  #mal=('지난해', 'Noun'), ('글로벌', 'Noun'),...
#         if not mal[1] in ['Alpha','Punctuation','Josa','Number','Eomi','Foreign']:
#             templist.append(mal[0])
#     # print(templist)
#     fw.write(' '.join(templist))
#---------------------
# from gensim.models import word2vec
# # data=word2vec.LineSentence('data\\news2.csv')   #단어 단어 단어
# # model=word2vec.Word2Vec(data,size=200,window=5,min_count=2,sg=1)
# # model.save('data\\news2.model')
# # ------------------
# model=word2vec.Word2Vec.load('data\\news2.model')
# print(model.most_similar('코로나',topn=3))
# print(model.most_similar('금융'))
# -----------------
# 1)네이버 api를 활용- 블러그에서 성탄절을 검색하여  description의 내용을 500건 수집하여
# blog.csv로 저장
# import os
# import sys
# import urllib.request
# import json
# with open('data\\blog.csv','w',encoding='utf-8') as f:
#     client_id = ""
#     client_secret = ""
#     encText = urllib.parse.quote("성탄절")
#     url = "https://openapi.naver.com/v1/search/blog?start={}&display=100&query=" + encText # json 결과
#     # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
#     for p in range(1,502,100):
#         request = urllib.request.Request(url.format(p))
#         request.add_header("X-Naver-Client-Id",client_id)
#         request.add_header("X-Naver-Client-Secret",client_secret)
#         response = urllib.request.urlopen(request)
#         rescode = response.getcode()
#         if(rescode==200):
#             response_body = response.read()
#             j1=response_body.decode('utf-8')
#         else:
#             print("Error Code:" + rescode)
#         dic=json.loads(j1)
#         # print(dic)
#         # print(dic['items'])   #[{},{} ,.....]
#         for d in dic['items']:
#             # print(d['description'].replace('<b>성탄절</b>','성탄절'))
#             f.write(d['description'].replace('<b>성탄절</b>','성탄절')+'\n')
# 2) 가장 많이 사용된 명사 10개와 그 횟수 출력
# from konlpy.tag import Okt
# with open('data\\blog.csv',encoding='utf-8') as f:
#     text=f.read()
# okt=Okt()
# word_dic={}  #{성탄절:3,트리:1,....}
# for line in text.split('\n'):
#     mal=okt.nouns(line)   #리스트
#     # print(mal)
#     for m in mal:
#         if not (m in word_dic):
#             word_dic[m]=0
#         word_dic[m]=word_dic[m]+1
#     # break
# # print(word_dic)
# # print(word_dic.items())
# s1=sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
# print(s1)
# 3)'선물'과 유사한 단어 출력
#단어 단어 단어 ------------------------
# from konlpy.tag import Okt
# with open('data\\blog.csv',encoding='utf-8') as f:
#     text=f.read()
# fw=open('data\\blog2.csv','w',encoding='utf-8')  #단어 단어 단어
# okt=Okt()
# for line in text.split('\n'):
#     mallist=okt.pos(line,norm=True,stem=True)
#     # print(mallist)   #[('유사', 'Noun'), ('이래', 'Adjective'),...]
#     temp=[]
#     for mal in mallist:
#         if not mal[1] in ['Josa','Punctuation','Determiner','Number','Foreign']:
#             temp.append(mal[0])
#     # print(temp)
#     # print(' '.join(temp))
#     fw.write(' '.join(temp))
# 모델생성
# from gensim.models import word2vec
# data=word2vec.LineSentence('data\\blog2.csv')
# model=word2vec.Word2Vec(data,size=200,window=5,sg=1)
# model.save('data\\blog2.model')
# 3)'선물'과 유사한 단어 출력
from gensim.models import word2vec
model=word2vec.Word2Vec.load('data\\blog2.model')
print(model.most_similar('선물'))