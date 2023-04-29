import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers,proxies={"https":"114.237.231.152:41224"}).text
    with open('3.html','w',encoding='utf-8') as fp:
        fp.write(page_text)