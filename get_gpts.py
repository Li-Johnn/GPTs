
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
import random
import subprocess

more_gpts = True
waiting = 5
path = "gpts3.txt"

def call_more_GPTs(driver):
    elements = driver.find_elements_by_css_selector("button > div.flex")[1:]

    for e in elements:
        try:
            e.click()
        except:
            pass


def get_GPTs_list(driver):
    # if driver.current_url != "https://chat.openai.com/gpts":
    #     driver.get("https://chat.openai.com/gpts")
    #     sleep(2)

    prefix = "https://chat.openai.com"
    html_text = driver.page_source
    matches = re.findall(r'"/g/g-.*?"', html_text)
    href_list = [match.strip('"') for match in matches]
    href_list = [h for h in href_list if not "/c/" in h]
    href_list = [prefix + url for url in href_list]
    return href_list

command = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--remote-debugging-port=9222',
    '--no-first-run',
    '--no-default-browser-check',
    "https://chat.openai.com/gpts"
]
process = subprocess.Popen(command)

sleep(waiting)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
if more_gpts:
    call_more_GPTs(driver)
    sleep(waiting)
    call_more_GPTs(driver)
    sleep(waiting)
href_list = get_GPTs_list(driver)

with open(path, "w") as f:
    for h in href_list:
        f.write(f"{h}\n")

sleep(waiting * 3.5)
process.terminate()