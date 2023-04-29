from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from lxml import etree
from multiprocessing.dummy import Pool
from time import sleep
import requests

if __name__ == '__main__':
    url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    drag_tag = browser.find_element(By.ID,'draggable')
    action = ActionChains(browser)
    action.click_and_hold(drag_tag)
    #调用perform方法才会执行
    for i in range(1,17):
        action.move_by_offset(17,0).perform()

    #停留2s
    action.pause(2).perform()
    #释放鼠标
    action.release().perform()
    #action = ActionChains(browser)
    #action.click(login_button)
    input()