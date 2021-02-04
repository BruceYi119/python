import os
import re
import time
import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikibook.co.kr']
    start_urls = ['http://wikibook.co.kr/list/']

    def parse(self, response):
        ul = response.css('ul#book-list')
        lis = ul.css('li')

        for li in lis[:3]:
            time.sleep(0.3)
            url = li.css('a.book-url::attr(href)').get()
            yield response.follow(url, self.bookDetail)

    def bookDetail(self, response):
        title = response.css('h1.main-title::text').get()
        subTitle = response.css('h2.sub-title::text').get()
        imgUrl = response.css('img.book-image-2d::attr(src)').get()
        reg = re.compile('(.jpg|.jpeg|.png){1}')
        ext = reg.findall(imgUrl)[0]
        fileName = '{}_{}{}'.format(title,str(time.time()).replace('.',''),ext)

        req = scrapy.Request(imgUrl,self.saveImg)
        req.meta['fileName'] = fileName
        yield req

    def saveImg(self, response):
        imgPath = os.path.join('..','img')

        if not os.path.exists(imgPath):
            os.mkdir(imgPath)

        with open(os.path.join('..','img',response.meta['fileName']), 'wb') as f:
            f.write(response.body)