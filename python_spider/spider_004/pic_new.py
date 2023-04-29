import requests

from lxml import etree

if __name__ == '__main__':
    url = "https://pic.netbian.com/tupian/29895.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    session = requests.session()
    tree = etree.HTML(session.get(url=url,headers=headers).text)
    tmp_url = tree.xpath('//*[@id="img"]/img/@src')[0]
    img_url = "https://pic.netbian.com" + tmp_url
    print(img_url)
    img_data = session.get(url=img_url,headers=headers).content
    with open('./test.jpg','wb') as fp:
        fp.write(img_data)