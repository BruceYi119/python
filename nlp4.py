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
from gensim.models import word2vec
# data=word2vec.LineSentence('data\\news2.csv')   #단어 단어 단어
# model=word2vec.Word2Vec(data,size=200,window=5,min_count=2,sg=1)
# model.save('data\\news2.model')
# ------------------
model=word2vec.Word2Vec.load('data\\news2.model')
print(model.most_similar('코로나',topn=3))
print(model.most_similar('금융'))
# -----------------
# 1)네이버 api를 활용- 블러그에서 성탄절을 검색하여  description의 내용을 500건 수집하여
# blog.csv로 저장
# 2) 가장 많이 사용된 명사 10개와 그 횟수 출력
# 3)'선물'과 유사한 단어 출력
# ------------------------


