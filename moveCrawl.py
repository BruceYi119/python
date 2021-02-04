# 영화제목 점수 (예매율), (상영시간)을 추출하여 data/movie.csv 저장
# 영화포스터는 img폴더에 저장

import os
import re
import time
import requests
from bs4 import BeautifulSoup

# 네어버 영화 사이트 주소
url = 'https://movie.naver.com/movie/running/current.nhn'
# 영화페이지 결과 텍스트로담기
html = requests.get(url).text
# 돔형태로 파싱
dom = BeautifulSoup(html, 'lxml')
# 무비의 기준태그 추출
moves = dom.find_all('dl', class_ = 'lst_dsc')
# 이미지의 기준태그 추출
imgs = dom.find_all('div', class_ = 'thumb')
# 상영시간 추출을 위한 정규식
timeReg = re.compile('[0-9]+분{1}')
# 이미지 확장자 추출을 위한 정규식
imtExtReg = re.compile('(.jpg|.gif|.png|.jpeg)')
#영화 데이터 (영화제목,점수,예매율,상영시간) 형식
result = []
# 영화제목 데이터
titles = []

# data/movie.csv 에 영화데이터 삽입
def fileWrite(result):
    # if os.path.exists(os.path.join('data','movie.csv')):
    #     os.remove(os.path.join('data','movie.csv'))

    dataTxt = '';

    for data in result:
        dataTxt += data;

    with open(os.path.join('data','movie.csv'), 'w', encoding='utf-8') as f:
        f.write(dataTxt)

# 영화데이터 추출
def makeMovieData():
    for move in moves:
        title = move.find('a').text
        score = move.find('div', class_ = 'star_t1').find('span', class_ = 'num').text

        if move.find('div', class_ = 'star_t1 b_star') and move.find('div', class_ = 'star_t1 b_star').find('span', class_ = 'num'):
            bookingRate = move.find('div', class_ = 'star_t1 b_star').find('span', class_ = 'num').text
        else:
            bookingRate = ''

        if len(timeReg.findall(move.find('dl', class_ ='info_txt1').find('dd').text)) > 0:
            time = timeReg.findall(move.find('dl', class_ = 'info_txt1').find('dd').text)[0]
        else:
            time = ''

        # result.append("%s,%s,%s,%s\n"%(title,score,bookingRate,time))
        result.append("{},{},{},{}\n".format(title,score,bookingRate,time))
        titles.append(title)

    fileWrite(result)

# 영화 이미지 복사
def makeImg():
    i = 0;

    for img in imgs:
        src = img.find('img')['src']
        img = requests.get(src)
        ext = imtExtReg.findall(src)[0]
        fileName = titles[i].replace(':',' -') + ext

        time.sleep(0.1)

        with open(os.path.join('img',fileName), 'wb') as f:
            if (img):
                f.write(img.content)

        i += 1

# 해당 파일에서만 함수 실행
if __name__ == '__main__':
    makeMovieData()
    makeImg()