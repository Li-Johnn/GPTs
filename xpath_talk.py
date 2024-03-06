import time
from selenium import webdriver 
# from selenium.webdriver.chrome.service import Service  

# Driver_path = r'E:\Programs\chrome-win64\chromedriver.exe'

# driver = webdriver.Chrome(executable_path = Driver_path)
driver = webdriver.Chrome()
driver.get('https://chat.openai.com')

driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]/div').click()
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/label/span[1]').click()
time.sleep(333)