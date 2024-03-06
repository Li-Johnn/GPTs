# Before running:
# execute '''start E:\Programs\chrome-win64\chrome.exe https://chat.openai.com --remote-debugging-port=9222''' in shell(Windows)
# different OS: https://chat.openai.com/share/d965e64c-4d58-4173-a8ff-832f6c748f32
# postfix --remote-debugging-port=9222
# mac:
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check www.google.com
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import random
# import pyautogui    # 备选，图形化界面点击

# maybe helpful for avoiding anti-reptile mechanism
waiting = True
# Chrome_Driver = r'E:\Programs\chrome-win64\chromedriver.exe'
msgs :list[str] = ["hello"]


def call_more_GPTs(driver):
    if driver.current_url != "https://chat.openai.com/gpts":
        driver.get("https://chat.openai.com/gpts")
        time.sleep(2)
    for i in range(6, 15):
        driver.find_element_by_xpath(f'//*[@id="__next"]/div[1]/div/main/div/div[2]/div[{i}]/div[2]/button').click()
        if waiting:
            time.sleep(random.uniform(0, 2))

def get_GPTs_list(driver):
    if driver.current_url != "https://chat.openai.com/gpts":
        driver.get("https://chat.openai.com/gpts")
        time.sleep(2)

    prefix = "https://chat.openai.com"
    html_text = driver.page_source
    matches = re.findall(r'"/g/g-.*?"', html_text)
    href_list = [match.strip('"') for match in matches]
    href_list = [prefix + url for url in href_list]
    return href_list

def send_msg(driver, msg):
    driver.find_element_by_id("prompt-textarea").send_keys(msg)
    while True:
        try:                   
            # driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/main/div[1]/div[2]/form/div/div/div/button').click()
            driver.find_element_by_css_selector("[data-testid='send-button']").click()
            break
        except:
            time.sleep(3)

def talk_with_GPTs(driver, url, msgs):
    # driver.get(url)
    time.sleep(2)
    for msg in msgs:
        print(msg)
        send_msg(driver, msg)
        if waiting:
            time.sleep(random.uniform(0, 5))



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(executable_path = Chrome_Driver, options=chrome_options)
# driver.get("https://chat.openai.com")
# urls = get_GPTs_list(driver)
# print(urls)
# urls = urls[:2]

talk_with_GPTs(driver, "https://chat.openai.com", msgs)
# for url in urls:
#     print(url)
#     talk_with_GPTs(driver, url, msgs)
#     time.sleep(10)

# try:
#     driver.find_element_by_xpath('//*[@id="prompt-textarea"]').send_keys("test")
# except:
#     driver.get("https://chat.openai.com")
#     time.sleep(3)
#     driver.find_element_by_xpath('//*[@id="prompt-textarea"]').send_keys("test")
# print("Typed")
# while True:
#     try:
#         driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/main/div[1]/div[2]/form/div/div[1]/div/button').click()
#         print("Sent")
#         break
#     except:
#         time.sleep(5)
# cookies = driver.get_cookies()

# driver.get("https://chat.openai.com/gpts")
# time.sleep(3)
# # See more
# for i in range(6, 15):
#     driver.find_element_by_xpath(f'//*[@id="__next"]/div[1]/div/main/div/div[2]/div[{i}]/div[2]/button').click()
# get_GPTs_list(driver)
    


# TODO: 绕过登录
# options = webdriver.ChromeOptions()
# # chrome中加入配置参数
# options.add_argument('--ignore-certificate-errors')
# driver2 = webdriver.Chrome(executable_path = r'E:\Programs\chrome-win64\chromedriver.exe', chrome_options=options)

# driver2.get("https://chat.openai.com")

# for cookie in cookies:
#     print(cookie)
#     driver2.add_cookie(cookie)
# driver2.get("https://chat.openai.com")

