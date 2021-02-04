# 네이버 Papago NMT API 예제
import os
import sys
import json
import urllib.request
client_id = "acy79LmJLZl4GQmxZYJu"
client_secret = "a09LS2bp2Q"
encText = urllib.parse.quote("세계 최강의 프로그램 언어는 무었인가?")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

r = json.loads(result)
print(r)
print(r['message']['result']['translatedText'])