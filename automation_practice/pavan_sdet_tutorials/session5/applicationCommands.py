import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.cricbuzz.com/")

# assert browser.find_element(By.XPATH, "//*[@title='India won by 6 runs']").text.split()[0] == "India"
#
# print(type(browser.find_element(By.XPATH, "//*[@title='India won by 6 runs']").text))
# print(browser.find_element(By.XPATH, "//*[@title='India won by 6 runs']").text.split()[0])
# time.sleep(3)

# application based commands

browser.get("https://www.cricbuzz.com/")

print(browser.title)

print(browser.current_url)

print(browser.page_source)



