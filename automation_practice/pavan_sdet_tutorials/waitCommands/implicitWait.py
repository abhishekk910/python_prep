import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(100)
browser.get("https://www.google.com/")

search_box = browser.find_element(By.NAME, 'q')
search_box.send_keys('Selenium')
search_box.submit()

browser.find_element(By.XPATH, "//h3[text()='Selenium']").click()

browser.close()