# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ImageDownloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print('%s.jpg 下载成功!' %item['name'])
        yield scrapy.Request(item['url'])

    def file_path(self, request, response=None, info=None, *, item):
        img_name = item['name'] + '.jpg'
        return img_name

    def item_completed(self, results, item, info):
        return item

class BossProPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        print("爬虫开始")
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='tupian')

    def process_item(self, item, spider):
        # print(item["title"],item["content"])
        self.cursor = self.conn.cursor()
        try:
            # print(self.conn)
            # self.cursor.execute("insert into xiaohua_content values('%s','%s')" %(item["titile"],item["content"]))
            sql = format("insert into tupian_data values('%s','%s')" %(item['name'],item['url']))
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()

        except Exception as e:
            print("执行出错")
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        print("爬虫结束")
        self.cursor.close()
        self.conn.close()
