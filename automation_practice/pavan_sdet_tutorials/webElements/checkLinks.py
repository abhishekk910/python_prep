import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://www.cricbuzz.com/')

elements = browser.find_elements(By.XPATH, "//a")

print(elements)
print(len(elements))

for element in elements:
    print(element.text)
