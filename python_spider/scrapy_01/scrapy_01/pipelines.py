# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class Scrapy01Pipeline(object):
    fp = None

    def open_spider(self,spider):
        print("爬虫开始")
        self.fp = open('data.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        title = item["title"]
        content = item["content"]
        self.fp.write(title + " " + content + "\n")
        return item
    def close_spider(self,spider):
        print("爬虫结束")
        self.fp.close()

class StoreMysqlPipeline(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        print("爬虫2开始")
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='xiaohua')

    def process_item(self,item,spider):
        #print(item["title"],item["content"])
        self.cursor = self.conn.cursor()
        try:
            #print(self.conn)
            #self.cursor.execute("insert into xiaohua_content values('%s','%s')" %(item["titile"],item["content"]))
            sql = "insert into xiaohua_content values('" + item["title"] + "','" + item["content"] + "')"
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()

        except Exception as e:
            print("执行出错")
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        print("爬虫2结束")
        self.cursor.close()
        self.conn.close()

