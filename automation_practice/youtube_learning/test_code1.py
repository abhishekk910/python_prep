from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cricbuzz.com")
time.sleep(2)

# Click on "Live Scores"
element = driver.find_element(By.LINK_TEXT, "Kolkata Knight Riders part ways with head coach Chandrakant Pandit")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(1)
element.click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Live Scores").click()

time.sleep(3)


