import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


browser.get("https://www.flipkart.com/")
time.sleep(2)

browser.get("https://www.amazon.in/")
time.sleep(2)

browser.back()
time.sleep(2)

browser.forward()
time.sleep(2)
browser.refresh()
time.sleep(2)