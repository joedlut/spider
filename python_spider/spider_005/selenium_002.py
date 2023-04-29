from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':
    url = "https://pic.netbian.com/4kdongman/index_7.html"
    option = ChromeOptions()
    option.add_argument("--proxy-server=https://121.205.177.63:23850")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"
    }
    s = Service('D:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s,options=option)
    #browser = webdriver.Chrome(service=s)
    browser.get(url)
    #page_text = browser.page_source
    #tree = etree.HTML(page_text)
    #while True:
    #    jump = browser.find_element(By.LINK_TEXT, '下一页')
    #    jump.click()
    #    sleep(2)
     #   print(jump)
    print(browser.page_source)
    input()