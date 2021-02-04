import requests
from bs4 import BeautifulSoup
# url = 'https://www.naver.com/'
# r = requests.get(url)
# print(r.text)
# print(r.headers)
# print(r.encoding)

# with open('data\\test.html', 'w', encoding='utf-8') as f:
#     f.write(r.text)

with open('data\\test.html', 'r', encoding='utf-8') as f:
    txt = f.read()

# dom = BeautifulSoup(r.text, 'html.parser')
dom = BeautifulSoup(txt, 'lxml')
# print(dom.find_all('div')[1])
# dom.find_all('태그', class_ = '클래스명')
# dom.find_all('태그', { 'class' = '클래스명' })
print(dom.find_all('div')[1].p)
print(dom.find_all('p', { 'class': 'p3' })[0].text)
print(dom.find('nav').attrs['data'])
print(dom.find(class_ = 'p3'))
# print(dom.find(id = 'footer'))
print(dom.find(id = 'footer').find_all('p')[2]['class'])
print(dom.find(id = 'footer').find_all('p')[2]['id'])