from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")

time.sleep(30)  # Let the page load

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-main-menu-item-wrapper")))
lists = driver.find_elements(By.CLASS_NAME, "oxd-main-menu-item-wrapper")
print(len(lists))
