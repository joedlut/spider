import json

import requests
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '13',
        'interval_id': '80:70',
        'action': '',
        'start': '0',
        'limit': '200'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,params=param,headers=headers)
    list_data = response.json()
    with open('./douban.json','w',encoding='utf-8') as fp:
        json.dump(list_data,fp=fp,ensure_ascii=False)
    print("finish")
