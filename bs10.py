import os
import sys
import json
import urllib.request

def translation():
    with open(os.path.join('data','dream.txt'), 'r', encoding='utf-8') as f:
        str = f.read()

    client_id = "acy79LmJLZl4GQmxZYJu"
    client_secret = "a09LS2bp2Q"
    encText = urllib.parse.quote(str)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    j = json.loads(response_body.decode('utf-8'))

    print(j['message']['result']['translatedText'])

translation()