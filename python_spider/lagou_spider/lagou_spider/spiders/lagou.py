import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    #allowed_domains = ['lagou.com']
    start_urls = ["https://www.lagou.com/wn/jobs?fromSearch=true&kd=java&city=%E6%B7%B1%E5%9C%B3&pn=1"]

    def parse(self, response):

