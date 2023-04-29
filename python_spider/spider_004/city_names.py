import requests

from lxml import etree

if __name__ == '__main__':
    url = "http://www.aqistudy.cn/historydata/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    names = []
    hot_list = etree.HTML(page_text).xpath('//div[@class="hot"]/div[2]/ul/li')
    for i in hot_list:
        names.append(i.xpath('./a/text()'))
    all_list = etree.HTML(page_text).xpath('//div[@class="all"]/div[2]/ul/div[2]/li')
    for i in all_list:
        names.append(i.xpath('./a/text()'))
    print(names)
    with open('./city_name.txt','w', encoding='utf-8') as fp:
        for name in names:
            fp.write(name[0])
            fp.write('\n')


