#!/usr/bin/python3
import requests
import os
from time import sleep
from lxml import etree

if __name__ == '__main__':
    url = "https://pic.netbian.com/4kmeinv/index.html"
    pic_dir = 'D:\pic_libs'
    proxies = {
        "https": "183.155.109.124:39111"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    tree = etree.HTML(requests.get(url=url, headers=headers).text)
    print(requests.get(url=url, headers=headers).text)
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)

    li_list = tree.xpath('/html/body/div[2]/div/div[3]/ul/li')
    print(li_list)
    for li in li_list:
        tmp_url = li.xpath('./a/@href')[0]
        page_url = "https://pic.netbian.com" + tmp_url
        tree1 = etree.HTML(requests.get(url=page_url, headers=headers).text)
        pic_url = "https://pic.netbian.com" + tree1.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@src')[0]
        name = tree1.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@alt')[0]
        name1 = name.encode('iso-8859-1').decode('gbk')
        file_name = name1 + ".jpg"
        with open(pic_dir + "\\" + file_name, 'wb') as fp:
            img_data = requests.get(url=pic_url, headers=headers).content

            fp.write(img_data)
            print(file_name, "下载成功！")
    for i in range(2, 125):
        url = "https://pic.netbian.com/4kmeinv/index_" + str(i) + ".html"
        tree = etree.HTML(requests.get(url=url, headers=headers).text)
        if not os.path.exists(pic_dir):
            os.mkdir(pic_dir)

        li_list = tree.xpath('/html/body/div[2]/div/div[3]/ul/li')
        for li in li_list:
            tmp_url = li.xpath('./a/@href')[0]
            page_url = "https://pic.netbian.com" + tmp_url
            tree1 = etree.HTML(requests.get(url=page_url, headers=headers).text)
            pic_url = "https://pic.netbian.com" + \
                      tree1.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@src')[0]
            name = tree1.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@alt')[0]
            name1 = name.encode('iso-8859-1').decode('gbk')
            file_name = name1 + ".jpg"
            with open(pic_dir + "\\" + file_name, 'wb') as fp:
                img_data = requests.get(url=pic_url, headers=headers).content
                fp.write(img_data)
                print(file_name, i, "下载成功！")