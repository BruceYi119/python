import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.naver.com/movie/running/current.nhn']
    start_urls = ['http://movie.naver.com/movie/running/current.nhn/']

    def parse(self, response):
        pass
