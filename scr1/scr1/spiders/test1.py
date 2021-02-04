import scrapy

class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['http://alexa.com/topsites/']

    def parse(self, response):
        trs = response.css('div.tr.site-listing')
        for tr in trs:
            tds = tr.css('div.td')
            yield {
                'rank': tds[0].css('::text').get(),
                'site': tds[1].css('a').xpath('@href').get(),
                'Daily Time on Site': tds[2].css('p::text').get(),
                'Daily Pageviews per Visitor': tds[3].css('p::text').get(),
                '% of Traffic From Search': tds[4].css('p::text').get(),
                'Total Sites Linking In': tds[5].css('p::text').get()
            }