import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com/")
driver.maximize_window()
time.sleep(30)

total = driver.find_elements(By.TAG_NAME, "a")
print(len(total))