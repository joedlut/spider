import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lxml import etree
from time import sleep

if __name__ == '__main__':
    url = "https://video.pearvideo.com/mp4/adshort/20180517/cont-1346772-12085786_adpkg-ad_hd.mp4"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    session = requests.session()
    img_data = session.get(url=url,headers=headers).content
    with open('./li.mp4','wb') as fp:
        fp.write(img_data)