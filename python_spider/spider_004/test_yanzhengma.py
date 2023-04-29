import requests
from lxml import etree
import json
import time
import base64
class YdmVerify(object):
    _custom_url = "https://www.jfbym.com/api/YmServer/customApi"
    _token = "Cb8eMX4CkXOa5S+ZK9j7IggkEYkn0eh1udgzMpTCHdc"
    _headers = {
        'Content-Type': 'application/json'
    }

    def common_verify(self, image, verify_type="10110"):
        payload = {
            "image": base64.b64encode(image).decode(),
            "token": self._token,
            "type": verify_type
        }
        resp = requests.post(self._custom_url, headers=self._headers, data=json.dumps(payload))
        print(resp.text)
        return resp.json()['data']['data']

if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    tree = etree.HTML(requests.get(url=url,headers=headers).text)
    rel_url = tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_url = "https://so.gushiwen.cn" + rel_url
    print(img_url)
    img_data = requests.get(img_url,headers=headers).content
    with open('1.xls', 'wb') as fp:
        fp.write(img_data)

    Y = YdmVerify()
    with open('test_2.jpg', 'rb') as f:
        s = f.read()
    data = Y.common_verify(s)
    print(data)

