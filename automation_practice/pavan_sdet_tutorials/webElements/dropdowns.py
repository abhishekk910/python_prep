import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


browser = webdriver.Chrome()

browser.implicitly_wait(60)
browser.maximize_window()
browser.get('https://rahulshettyacademy.com/AutomationPractice/')

dropValue= Select(browser.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))

# dropValue.select_by_value("option1")
# dropValue.select_by_visible_text("Option2")
# dropValue.select_by_index(3)
# time.sleep(5)

# allOptions = dropValue.options

# for option in allOptions:
#     print(option.text)

# for option in allOptions:
#     if option.text == 'Option2':
#         option.click()
#         break
#
# time.sleep(10)


allOptions=browser.find_elements(By.XPATH,'//*[@id="dropdown-class-example"]/option')
# print(len(allOptions))

for option in allOptions:
    if option.text == 'Option2':
        option.click()
        break

time.sleep(10)