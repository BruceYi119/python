import os
import sys
import urllib.request
import json
client_id = "BB9aY0rt7wzFgrhTbjeN"
client_secret = "O2JtfY1AIt"
encText = urllib.parse.quote("python")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
d1=json.loads(result)
# print(d1)
# print(type(d1))
#
# title,description의 내용 출력
print(d1['items'])      #[{},{},{},...]
for doc in d1['items']:  #doc={}
    print(doc['title'])
    print(doc['description'])
    print('-'*30)
# 번역접근







