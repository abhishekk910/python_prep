from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Step 1: Start browser
driver = webdriver.Firefox()

# Step 2: Open login page
driver.get("https://10.189.96.189")
driver.maximize_window()

# Optional: Wait for page to load fully
time.sleep(3)

# Step 3: Locate Username field using placeholder text and enter username
username_input = driver.find_element(By.XPATH, "//label[text()='Username']/following::input[1]")
username_input.send_keys("3paradm")

# Step 4: Locate Password field using label and enter password
password_input = driver.find_element(By.XPATH, "//label[text()='Password']/following::input[1]")
password_input.send_keys("3pardata25")

# Step 5: Click Log In button
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]")
login_button.click()

# Optional: Wait to see result before browser closes
time.sleep(5)

# Step X: Click on the DriveCage button using its aria-label
# Click the button *next to* the span containing "System"
system_button = driver.find_element(By.XPATH, "//span[text()='System']/following::button[1]")
system_button.click()

time.sleep(5)


wait = WebDriverWait(driver, 15)

controllers_tile = wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//span[text()='Controllers']/ancestor::div[contains(@class, 'ssmci-dashboardtile')]"
)))
controllers_tile.click()
print("✅ Clicked Controllers tile")


node0_tile = wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//div[contains(@class, 'StyledBox-sc-13pk1d4-0') and contains(@class, 'dvjorv')]"  # div with both classes
    "[.//h3[contains(text(),'Node 0')]]"  # that contains an h3 with text Node 0
)))

node0_tile.click()
print("✅ Clicked Node 0 tile")



time.sleep(5)

from selenium.webdriver.common.by import By

mezzanine_value_elem = wait.until(
    EC.visibility_of_element_located((
        By.XPATH,
        "//tr[@class='grommetux-table-row'][.//label[text()='Mezzanine card']]//span[contains(@class, 'ssmci-detailspanelitem-value')]"
    ))
)
value_text = mezzanine_value_elem.text.strip()
print("Mezzanine card value:", value_text)

assert value_text.lower() in ("yes", "no"), f"Unexpected value: {value_text}"

# Optional: act or log based on exact value
if value_text.lower() == "yes":
    print("✅ Mezzanine card is enabled (YES).")
else:
    print("⚠️ Mezzanine card is not present.")


time.sleep(5)

driver.quit()
