import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://demo.nopcommerce.com/")

# find element - single web element
# search_element = browser.find_element(By.ID, "small-searchterms")
# search_element.send_keys("Apple")


# browser.find_element(By.XPATH, "//button[@type='submit']").click()

# find element - locator matching with multiple elements

# search_element = browser.find_element(By.XPATH, "//div[@class='footer']//a11")
# print(search_element.text)



# --------  find elements

# search_element = browser.find_elements(By.ID, "small-searchterms")
# search_element[0].send_keys("Apple")

# time.sleep(2)

# search_elements = browser.find_elements(By.XPATH, "//div[@class='footer']//a")
#
# for ele in search_elements:
#     # print(ele.text)
#     ele.click()
#     time.sleep(3)
#     browser.back()
#     time.sleep(3)

