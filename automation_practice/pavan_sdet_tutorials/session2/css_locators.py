from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')
time.sleep(3)
driver.maximize_window()

#tag and id
# driver.find_element(By.CSS_SELECTOR, "input#email" ).send_keys("testing")
# driver.find_element(By.CSS_SELECTOR, "#email" ).send_keys("testing")


# tag and class
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("testing.com")
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("testing.com")


#tag and attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal-email]").send_keys("testing.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal-email]").send_keys("testing.com")


#tag, class and attribute
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal-pass]").send_keys("1234")
driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid=royal-pass]").send_keys("1234")
time.sleep(3)
# driver.find_element(By.CLASS_NAME, "_9lsb").click()
driver.find_element(By.CSS_SELECTOR, "div._9lsb").click()
time.sleep(3)