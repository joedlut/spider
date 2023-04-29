import requests
from lxml import etree
import os

if __name__ == '__main__':
    url = 'https://pic.netbian.com/4kmeinv/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    page_text = response.text
    li_list = etree.HTML(page_text).xpath('//div/ul[@class="clearfix"]/li')
    if not os.path.exists('./pic_libs'):
        os.mkdir('./pic_libs')
    for li in li_list:
        tmp_url = li.xpath('./a/img/@src')[0]
        pic_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        pic_name = pic_name.encode('iso-8859-1').decode('gbk')
        img_url = "https://pic.netbian.com/" + tmp_url
        img_data = requests.get(url=img_url,headers=headers).content
        img_path = './pic_libs/' + pic_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(pic_name, '下载成功！')


    print("ok")