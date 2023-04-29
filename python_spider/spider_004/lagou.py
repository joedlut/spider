import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from lxml import etree
from time import sleep
import requests
import re
from selenium.webdriver import ActionChains
from PIL import Image

if __name__ == "__main__":
    url = "https://www.lagou.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    browser.execute_script('document.body.style.zoom="0.4"')
    browser.get(url=url)

    page_text = browser.page_source

    city_tab = browser.find_element(By.XPATH,'//*[@id="changeCityBox"]/ul/li[6]/a')
    city_tab.click()

    #login_tab = browser.find_element(By.XPATH,'//*[@id="lg_tbar"]/div[1]/div[2]/ul/li[1]')
    search = browser.find_element(By.ID,'search_input')
    search.send_keys("Java")
    print(search)

    #search_button = browser.find_element(By.ID,'search_button')
    search_button = browser.find_element(By.XPATH,'//*[@id="search_button"]')
    search_button.click()

    page_text = browser.page_source

    #print(page_text)
    match_list = re.findall('name="password"',page_text)
    if len(match_list) > 0:
        click = browser.find_element(By.XPATH, '//*[@id="lg-passport-box"]/div/div[2]/div/div[4]/div[2]/div')
        print(click)
        click.click()
        username = browser.find_element(By.NAME, 'account')
        password = browser.find_element(By.NAME, 'password')
        username.send_keys('13189725929')
        password.send_keys('Ab@123456')
        login_button = browser.find_element(By.XPATH ,'//*[@id="lg-passport-box"]/div/div[2]/div/div[3]/button')
        login_button.click()
        # sleep 3s 等验证码信息加载出来
        time.sleep(3)
        page_text = browser.page_source
        match_list = re.findall(r'请拖动滑块', page_text)
        if len(match_list) > 0:
            print('hello')
            #print(page_text)
            #slider = browser.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]')
            #action = ActionChains(browser)
            #action.click_and_hold(slider)
            #action.move_by_offset(100, 0).perform()
            #slider = browser.find_element(By.XPATH,'//div[@class="geetest_btn_bb7edd54 geetest_btn"]')
            slider = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[3]')
            action = ActionChains(browser)
            action.click_and_hold(slider).perform()
            action.move_by_offset(130,0).perform()
            print(slider)
            browser.save_screenshot('./aa.png')
            img_ele = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]')
            print(img_ele)
            location = img_ele.location
            size = img_ele.size
            rangle = (
                int(location['x']), int(location['y']), int(location['x'] + size['width']),
                int(location['y'] + size['height'])
            )
            print(rangle)
            print(location)
            print(size)
            image = Image.open('./aa.png')
            code_img = 'code.png'
            frame = image.crop(rangle)
            frame.save(code_img)

        # 请在下图依次点击
        else:
            print("hello1")
            browser.save_screenshot('./aa.png')
            img_ele = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]')
            location = img_ele.location
            size = img_ele.size
            rangle = (
                int(location['x']),int(location['y']),int(location['x'] + size['width']),int(location['y'] + size['height'])
            )
            print(rangle)
            print(location)
            print(size)
            image = Image.open('./aa.png')
            code_img = 'code.png'
            frame = image.crop(rangle)
            frame.save(code_img)

    else:
        shenzhen = browser.find_element(By.XPATH, '//*[@id="jobsContainer"]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[4]')
        shenzhen.click()
        tree = etree.HTML(browser.page_source)
        job_list = tree.xpath('//*[@id="jobList"]/div[1]/div')
        print(job_list)


    input()



