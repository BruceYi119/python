import os
import scrapy

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.naver.com/movie/running/current.nhn']
    start_urls = ['http://movie.naver.com/movie/running/current.nhn']

    def parse(self, response):
        ul = response.css('ul.lst_detail_t1')
        lis = ul.css('li')

        for li in lis:
            tickRate = '0.00'

            if li.css('dd.star > dl.info_exp div.star_t1.b_star span.num::text'):
                tickRate = li.css('dd.star > dl.info_exp div.star_t1.b_star span.num::text').get()

            try:
                yield {
                    'title': str(li.css('dt.tit > a::text').get()).replace(',',''),
                    'score': li.css('dd.star span.num::text').get(),
                    'tickRate': tickRate
                }
            except:
                print('exception!')