import os
import re
import sys
import json
import urllib.request
from konlpy.tag import Okt
from gensim.models import word2vec

client_id = "BQ1uoKa6ERSfHgNoDpx7"
client_secret = "vu9DMk8ZJq"
encText = urllib.parse.quote("추석")

# 1)
def search(start = 1):
    url = 'https://openapi.naver.com/v1/search/blog?query={}&start={}&display=100'.format(encText, start)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        data = response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)

    return data

def save():
    str = ''
    for i in range(1, 500, 100):
        data = json.loads(search(i))
        for row in data['items']:
            s = row['description']
            # 등등 특수문자가 많아서 이정도로 생략...(대충제거)
            s = re.sub(r'(\<[a-z]+\>|\<\/[a-z]+\>|\‘|\’|\.+|\,|\^ㅅ\^|\?|\#|\[|\]|\:+|\'+|\!+)', '', s)
            str += '{} '.format(s)

    with open(os.path.join('data','YiSeungJun.txt'), 'w', encoding='utf-8') as f:
        f.write(str[:-1])

# save()

# 2)
okt = Okt()
data = open(os.path.join('data','YiSeungJun.txt'), encoding='utf-8').read()
data = data.split(' ')
dic = {}
for line in data:
    mlist = okt.nouns(line)
    for m in mlist:
        if m not in dic:
            dic[m] = 0
        dic[m] = dic[m]+1

nlist = sorted(dic.items(), key=lambda x:x[1], reverse=True)
# print(nlist[:30])

# 3)
# data = word2vec.LineSentence(os.path.join('data','YiSeungJun.txt'))
# model = word2vec.Word2Vec(data, size=200, window=5, min_count=2, sg=1)
# model.save(os.path.join('data','YiSeungJun.model'))

# 4)
model = word2vec.Word2Vec.load(os.path.join('data','YiSeungJun.model'))
print(model.most_similar('선물'))