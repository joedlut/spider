from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from lxml import etree
from multiprocessing.dummy import Pool
from time import sleep
import requests

if __name__ == '__main__':
    url = "https://www.pearvideo.com/panorama"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    tree = etree.HTML(requests.get(url=url, headers=headers).text)
    li_list = tree.xpath('//*[@id="categoryList"]/li')

    browser.get(url)
    page_text = browser.page_source
    tree1 = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="categoryList"]/li')
    for i in range(1, 11):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(1)
    page_text2 = browser.page_source
    tree2 = etree.HTML(page_text2)
    li_list = tree2.xpath('//*[@id="categoryList"]/li')
    url_list = []
    input()
