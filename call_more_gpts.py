from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import random

waiting = True

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
elements = driver.find_elements_by_css_selector("button > div.flex")[1:]

print(len(elements))

for i, e in enumerate(elements):
    e.click()