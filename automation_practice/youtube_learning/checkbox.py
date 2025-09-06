import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://artoftesting.com/samplesiteforselenium")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.find_element(By.CLASS_NAME, "Automation").click()
browser.maximize_window()

time.sleep(3)

browser.quit()