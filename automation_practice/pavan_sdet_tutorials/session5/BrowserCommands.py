

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)

browser.find_element(By.PARTIAL_LINK_TEXT, "Orange").click()

time.sleep(25)

browser.close()

time.sleep(10)