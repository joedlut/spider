from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    url = "https://news.163.com/domestic/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(url)
    for i in range(1, 11):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(1)


    more_click = browser.find_element(By.XPATH,'/html/body/div/div[3]/div[3]/div[1]/div[1]/div/a/div[1]/span')
    more_click.click()
    sleep(2)
    page_text = browser.page_source
    print(page_text)
    input()