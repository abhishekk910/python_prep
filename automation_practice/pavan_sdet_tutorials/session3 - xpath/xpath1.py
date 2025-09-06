from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.cricbuzz.com/")
driver.maximize_window()

# relative xpath

"""
//tagname[@attribute='value']
//*[@attribute='value']
"""
driver.find_element(By.XPATH, "//a[@title='Live Cricket Score']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[@title='Teams Schedule']").click()
time.sleep(3)

