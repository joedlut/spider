import scrapy
from boss_pro.items import BossProItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['https://pic.netbian.com/4kmeinv/index.html']
    start_urls = ['https://pic.netbian.com/4kmeinv/index.html']

    url = "https://pic.netbian.com/4kmeinv/index_%d.html"
    page_num = 2


    def parse_img_url(self, response):
        url = response.xpath('//*[@id="img"]/img/@src').extract_first()
        pic_url = "https://pic.netbian.com" + url
        #print(pic_url)
        item = response.meta['item']
        item['url'] = pic_url
        # 注意是 yield item
        yield item

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            url = li.xpath('./a/@href').extract()[0]
            name = li.xpath('./a/img/@alt').extract()[0]

            item = BossProItem()
            item['name'] = name
            jump_url = "https://pic.netbian.com" + url
            #print(jump_url)
            #注意是 self.parse_img_url,一定要加yield, 传递meta字段  ，不在一个页面中，所有要用meta 传给下个parse
            yield scrapy.Request(jump_url,callback=self.parse_img_url,meta={'item':item})

        if self.page_num < 72:
            new_url = format(self.url %self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)



