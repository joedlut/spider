from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lxml import etree
from time import sleep
import requests
#from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':
    url = "https://www.pearvideo.com/panorama"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    # 这里不能设置成无头，不然获取不到mp4地址
    #chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    #tree = etree.HTML(requests.get(url=url, headers=headers).text)
    #li_list = tree.xpath('//*[@id="categoryList"]/li')

    browser.get(url)
    for i in range(1, 11):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(1)
    page_text2 = browser.page_source
    tree2 = etree.HTML(page_text2)
    li_list = tree2.xpath('//*[@id="categoryList"]/li')
    print(li_list)
    url_list = []
    for li in li_list:
        tag = li.xpath('./div/a/@href')[0]
        if "video" not in tag:
            continue
        page_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
        video_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        # print(video_name)
        browser.get(page_url)
        sleep(1)
        page_text = browser.page_source
        tree = etree.HTML(page_text)
        #print(page_text)
        video_path = tree.xpath('//*[@id="JprismPlayer"]/video/@src')[0]
        dic = {
            'name': video_name,
            'url': video_path,
        }
        #print(page_url)
        print(video_path,video_name)
        url_list.append(dic)

    for i in url_list:
        print(i)
    input()
