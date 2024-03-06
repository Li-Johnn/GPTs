# Before running:
# execute '''start E:\Programs\chrome-win64\chrome.exe https://chat.openai.com --remote-debugging-port=9222''' in shell(Windows)
# different OS: https://chat.openai.com/share/d965e64c-4d58-4173-a8ff-832f6c748f32
# postfix --remote-debugging-port=9222
# mac:
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check www.google.com


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import random
import subprocess
# import pyautogui    # 备选，图形化界面点击

# maybe helpful for avoiding anti-reptile mechanism
waiting = True
# Chrome_Driver = r'E:\Programs\chrome-win64\chromedriver.exe'
msgs :list[str] = ["hello", "what can you do for me?"]

def get_gpts(path = "gpts2.txt"):
    with open(path, "r") as f:
        url_list = f.readlines()
        url_list = [url.strip() for url in url_list]
    return url_list

def send_msg(driver, msg):
    print("sleeping")
    driver.find_element_by_id("prompt-textarea").send_keys(msg)
    while True:
        try:                   
            # driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/main/div[1]/div[2]/form/div/div/div/button').click()
            driver.find_element_by_css_selector("[data-testid='send-button']").click()
            break
        except:
            sleep(3)
    sleep(10)

def talk_with_GPTs(url, msgs, port = 9222):
    command = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--remote-debugging-port=9222',
        '--no-first-run',
        '--no-default-browser-check',
        url
    ]
    process = subprocess.Popen(command)
    sleep(5)
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=chrome_options)

    for msg in msgs:
        send_msg(driver, msg)
    process.terminate()
    

urls = get_gpts()
urls = urls[:2]
for i, url in enumerate(urls):
    talk_with_GPTs(url, msgs, 9222)