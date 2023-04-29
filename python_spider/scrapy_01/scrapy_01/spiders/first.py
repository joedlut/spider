import scrapy
from scrapy_01.items import Scrapy01Item
class FirstSpider(scrapy.Spider):
    name = 'first'
    # 一般不使用allowed_domains  因为要爬取的图片域名地址不一定跟最初爬取的是一个域名
    #allowed_domains = ['www.baidu.com']
    start_urls = []
    for i in range(1, 2):
        url = 'http://www.xiaohua8.com/xiaohua/dongwuxiaohua_' + str(i)
        start_urls.append(url)
    print(start_urls)
    # response
    def parse(self, response):
        #print(response.text)
        li_list = response.xpath('//*[@id="newll1"]')
        data_list = []
        for li in li_list:
            # xpath 返回的是一个列表，每一个列表元素是一个Selector对象，需要用extract()方法提取对应的内容，extract()返回的是对应的内容列表
            #如果只有一个元素可以用 extract_first()
            title = li.xpath('./a/text()').extract_first()
            content = ' '.join(li.xpath('./div/text()').extract()).strip()
            item = Scrapy01Item()
            item["title"] = title
            item["content"] = content

            # 注意是，是用yield
            yield item
            # spider crawl first -o data.csv  持久化数据到文件中

        #return data_list