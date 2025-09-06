from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# self
# print(driver.find_element(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/self::a").text)


# parent
# print(driver.find_element(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/parent::td").text)

# child
# print(len(driver.find_elements(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/ancestor::tr/child::td")))

# ancestor
# print(driver.find_element(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/ancestor::tr").text)

# descendant
# print(len(driver.find_elements(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/ancestor::tr/descendant::*")))


# following
# print(len(driver.find_elements(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/ancestor::tr/following::*")))


# following-sibling
# print(len(driver.find_elements(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/ancestor::tr/following-sibling::*")))


# preceding
print(len(driver.find_elements(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/ancestor::tr/preceding::tr")))

# print(len(driver.find_elements(By.XPATH, "//a[text()='TVS Motor Co. Ltd.']/ancestor::tr/preceding-sibling::*")))

time.sleep(3)