import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://rahulshettyacademy.com/AutomationPractice/')

elements = browser.find_elements(By.XPATH, "//input[@type='checkbox']")

for element in elements:
    element.click()

time.sleep(3)

for element in elements:
    if element.is_displayed():
        element.click()