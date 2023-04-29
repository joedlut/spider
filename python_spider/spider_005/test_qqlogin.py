from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

if __name__ == '__main__':
    url = "https://qzone.qq.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(url)
    browser.switch_to.frame('login_frame')
    a_tag = browser.find_element(By.ID,'switcher_plogin')
    a_tag.click()

    uin_area = browser.find_element(By.ID,'u')
    pwd_area = browser.find_element(By.ID,'p')
    uin_area.send_keys('2532771263')
    pwd_area.send_keys('12almtks@_8')
    login_button = browser.find_element(By.ID,'login_button')
    login_button.click()
    sleep(3)
    print(browser.page_source)
    #action = ActionChains(browser)
    #action.click(login_button)


    input()