import scrapy


class TupianSpider(scrapy.Spider):
    name = 'tupian'
    #allowed_domains = ['pic.netbian.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']

    url = "https://pic.netbian.com/4kmeinv/index_%d.html"
    page_num = 2
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            img_name = li.xpath("./a/img/@alt").extract_first()
            print(img_name)
        if self.page_num < 5:
            new_url = format(self.url %self.page_num)
            self.page_num += 1
            #自动进行请求发送
            yield scrapy.Request(url=new_url,callback=self.parse)






