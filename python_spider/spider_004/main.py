import requests

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    with open("./kfc.txt",'w+',encoding='utf-8') as fp:
        for i in range(1, 15):
            param = {
                'cname': '',
                'pid': '',
                'keyword': '北京',
                'pageIndex': i,
                'pageSize': '10'
            }
            response = requests.post(url=url, data=param, headers=headers)
            page_text = response.text
            fp.write(page_text)
            fp.write('\n')
            print(i)
    print("finish")



