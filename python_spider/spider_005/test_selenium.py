from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lxml import etree
from multiprocessing.dummy import Pool
from time import sleep
import requests
def download_video(dic):
    name = dic['name']
    url = dic['url']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    video_data = requests.get(url=url,headers=headers).content
    with open(name,'wb') as fp:
        fp.write(video_data)
    print(name,'下载成功！')

if __name__ == '__main__':
    url = "https://www.pearvideo.com/panorama"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    tree = etree.HTML(requests.get(url=url, headers=headers).text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
    pool = Pool(4)
    video_list = []
    
    for li in li_list:
        page_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
        video_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        #print(video_name)
        browser.get(page_url)
        page_text = browser.page_source
        tree = etree.HTML(page_text)
        video_path = tree.xpath('//*[@id="JprismPlayer"]/video/@src')[0]
        #print(video_path)
        dic = {
            'name':video_name,
            'url':video_path,
        }
        video_list.append(dic)

    print(video_list)
    pool.map(download_video,video_list)
    pool.close()
    pool.join()
