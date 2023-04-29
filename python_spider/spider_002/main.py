import json

import requests

if __name__ == '__main__':
    post_url = "https://fanyi.baidu.com/sug"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/108.0.0.0 Safari/537.36'
    }
    keyword = input("input the word:")
    data = {
        'kw': keyword
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    dict_obj = response.json()
    fileName = keyword + '.json'
    with open(fileName, 'w', encoding='utf-8') as fp:
        json.dump(dict_obj, fp=fp, ensure_ascii=False)

    print("over")

