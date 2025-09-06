import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.cricbuzz.com")

viewports = [(414, 896), (430, 932), (1024, 1366), (344, 882)]
try:
    for viewport in viewports:
        driver.set_window_size(viewport[0], viewport[1])
        time.sleep(3)

finally:
    driver.close()


