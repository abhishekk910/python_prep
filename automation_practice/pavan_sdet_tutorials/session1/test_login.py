from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")

time.sleep(10)  # Let the page load

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)
print("logged in successfully")

if driver.title == "OrangeHRM":
    print("Title is same")
else:
    print("Title is not same")

driver.quit()


