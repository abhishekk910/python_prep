import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)
# ID and NAME
# driver.find_element(By.ID, "small-searchterms").send_keys('Apple iPhone 16 128GB')
# driver.find_element(By.NAME, "q").send_keys('Apple iPhone 16 128GB')


# Link Text and Partial Link Text
# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "R").click()

time.sleep(3)