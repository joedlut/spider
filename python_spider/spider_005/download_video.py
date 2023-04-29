import requests
import re
from lxml import etree
import selenium

if __name__ == '__main__':
    url = "https://www.pearvideo.com/panorama"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    tree = etree.HTML(requests.get(url=url,headers=headers).text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
    for li in li_list:
        page_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
        page_text = requests.get(url=page_url,headers=headers).text
        print(page_url)
