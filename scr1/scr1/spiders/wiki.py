import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikibook.co.kr/list/']
    start_urls = ['http://wikibook.co.kr/list/']

    def parse(self, response):
        lis = response.css('ul#book-list > li')

        for li in lis:
            print(li.css('h4.main-title::text').get())
            print(li.css('div.sub-title::text').get())
            print(li.css('span.author::text').get())
            break