
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import random

waiting = True

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
    href_list = [h for h in href_list if not "/c/" in h]
    href_list = [prefix + url for url in href_list]
    return href_list

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
href_list = get_GPTs_list(driver)

with open("gpts2.txt", "w") as f:
    for h in href_list:
        f.write(f"{h}\n")