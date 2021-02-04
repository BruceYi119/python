import requests
from bs4 import BeautifulSoup

url = "https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp"
data = {
    "S_PAGENUMBER": "2",
    "S_MB_CD": "W0726200",
    "S_HNAB_GBN": "",
    "hanmb_nm": "G - DRAGON",
    "sort_field": "SORT_PBCTN_DAY"
}
r = requests.post(url, data = data)
dom = BeautifulSoup(r.text, 'lxml')
table = dom.find_all('table')[1]

print(table)