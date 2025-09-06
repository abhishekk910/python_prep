import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://demo.nopcommerce.com/login")

# element = browser.find_element(By.XPATH, "//input[@id='newsletter-email']")
# print(element.text)
# print(element.get_attribute("placeholder"))

# time.sleep(5)
element = browser.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print()
print(element.text)
print(element.get_attribute("type"))