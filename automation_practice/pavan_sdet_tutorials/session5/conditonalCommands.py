


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://demo.nopcommerce.com/register")

# is_displayed(), is_enabled()

# assert browser.find_element(By.XPATH, "//input[@placeholder='Search']").is_displayed() == True

# assert browser.find_element(By.XPATH, "//button[@title='Search' and @aria-label='Search']").is_enabled() == False

male_radio = browser.find_element(By.XPATH, "//input[@id='gender-male']")
female_radio = browser.find_element(By.XPATH, "//input[@id='gender-female']")

male_radio.click()

# is_selected()
print(male_radio.is_selected(), female_radio.is_selected())

female_radio.click()

print(male_radio.is_selected(), female_radio.is_selected())

