# -*- coding:utf-8 -*-
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

if __name__ == '__main__':
    url = 'https://sz.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(url)
    page_text = browser.page_source
    tree = etree.HTML(page_text)
    property_list = tree.xpath('//div[@tongji_tag="fcpc_ersflist_gzcount"]')
    while True:
        for property in property_list:
            property_title = property.xpath('./a/div[@class="property-content"]/div/div/h3/text()')[0]
            property_price_num = \
                property.xpath(
                    './a/div[@class="property-content"]/div/p/span[@class="property-price-total-num"]/text()')[0]
            property_price_text = \
                property.xpath(
                    './a/div[@class="property-content"]/div/p/span[@class="property-price-total-text"]/text()')[0]
            property_average_price = \
                property.xpath('./a/div[@class="property-content"]/div/p[@class="property-price-average"]/text()')[0]
            price = property_price_num + property_price_text
            property_data = property.xpath('./a/div[@class="property-content"]/div/section/div[1]/p[2]/text()')[
                0].strip()
            address1 = property.xpath('./a/div[@class="property-content"]/div/section/div[2]/p[1]/text()')[0].strip()
            addr1 = property.xpath('./a/div[@class="property-content"]/div/section/div[2]/p[2]/span[1]/text()')[0].strip()
            addr2 = property.xpath('./a/div[@class="property-content"]/div/section/div[2]/p[2]/span[2]/text()')[0].strip()
            addr3 = property.xpath('./a/div[@class="property-content"]/div/section/div[2]/p[2]/span[3]/text()')[0].strip()
            address2 = addr1 + ' ' + addr2 + ' ' + addr3
            data = property_title + "," + price + "," + property_data + "," + address1+ ',' + address2 + ',' +  property_average_price
            print(data)
        next_click_tag = browser.find_element(By.LINK_TEXT, u'下一页')
        sleep(2)
        next_click_tag.click()
        page_text = browser.page_source
        tree = etree.HTML(page_text)
        property_list = tree.xpath('//div[@tongji_tag="fcpc_ersflist_gzcount"]')
    input()




