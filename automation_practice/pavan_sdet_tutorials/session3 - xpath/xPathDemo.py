from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.youtube.com/")
# driver.get("https://www.cricbuzz.com/")
# driver.implicitly_wait(5)
#
# driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("Coolie Trailer")
#
# driver.implicitly_wait(3)
#
# driver.find_element(By.XPATH, "//button[@title='Search']").send_keys("Coolie Trailer")
#
# driver.implicitly_wait(3)


# absolute xpath/Full xpath
# driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/form/input").send_keys("Coolie Trailer")
# driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/button").click()

# xpath with operators and & or
# driver.find_element(By.XPATH, "//input[@name='search_query' or @placeholder='Search']").send_keys("Coolie Trailer")
# driver.find_element(By.XPATH, "//button[@aria-label='Search' and @title='Search']").click()
# time.sleep(3)


# contains() and start-with()
# driver.find_element(By.XPATH, "//input[contains(@name, 'search')]").send_keys("Coolie Trailer")
# driver.find_element(By.XPATH, "//button[starts-with(@title, 'Se')]").click()
# time.sleep(3)


# text()
# driver.find_element(By.XPATH, "//a[text()='Rankings']").click()
driver.find_element(By.XPATH, "//yt-formatted-string[text()='Subscriptions']").click()
time.sleep(3)