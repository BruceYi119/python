# https://github.com/lumyjuwon/KoreaNewsCrawler

# import os
# import sys
# import json
# import re
import numpy as np
from PIL import Image
# import urllib.request
from konlpy.tag import Okt
import matplotlib.pyplot as plt
# from konlpy.tag import Hannanum
from wordcloud import WordCloud, STOPWORDS
# from korea_news_crawler.sportcrawler import SportCrawler
# from korea_news_crawler.articlecrawler import ArticleCrawler
# from multiprocessing import freeze_support

# Spt_crawler = SportCrawler()
# Spt_crawler.set_category('피겨스케이팅','김연아')
# Spt_crawler.set_date_range(2020,1,2021,2)
# Spt_crawler.start()

# if __name__ == '__main__':
#     freeze_support()
#     c = ArticleCrawler()
#     c.set_category('economy')
#     c.set_date_range(2021,1,2021,2)
#     c.start()