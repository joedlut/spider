import requests

if __name__ == '__main__':
    url = "https://news.163.com/domestic/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    page_text = requests.get(url=url,headers=headers).text
    print(page_text)