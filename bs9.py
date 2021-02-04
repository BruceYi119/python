# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import json
import urllib.request

client_id = "tUVE31gRkWWthXP_N4za"
client_secret = "ojSoGAcHkZ"
encText = urllib.parse.quote("성탄절")

def writeBlogCsv():
    data = '';

    for i in range(1, 1001, 100):
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100&start=101"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
        else:
            print("Error Code:" + rescode)

        j = json.loads(response_body.decode('utf-8'))['items']
        title = json['title']
        description = json['description']
        data += '{}::{}\n'.format(title,description)

    # with open(os.path.join('data',''))
writeBlogCsv()