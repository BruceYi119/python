# 영화제목 점수 (예매율), (상영시간)을 추출하여 data/movie.csv 저장
# 영화포스터는 img폴더에 저장

import os
import re
import time
import requests
import pymysql as my
from bs4 import BeautifulSoup

# 네어버 영화 사이트 주소
url = 'https://movie.naver.com/movie/running/current.nhn'
# 영화페이지 결과 텍스트로담기
html = requests.get(url).text
# 돔형태로 파싱
dom = BeautifulSoup(html, 'lxml')
# 무비의 기준태그 추출
moves = dom.find_all('dl', class_ = 'lst_dsc')
# 상영시간 추출을 위한 정규식
timeReg = re.compile('[0-9]+분{1}')

# 영화데이터 추출
def makeMovieData():
    con = my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
    cur = con.cursor(my.cursors.DictCursor)
    sql = 'insert into movie (title,score,bookingrate,time) values (%s,%s,%s,%s)'

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

        cur.execute(sql, (title,score,bookingRate,time))
        con.commit()

    con.close()

makeMovieData()