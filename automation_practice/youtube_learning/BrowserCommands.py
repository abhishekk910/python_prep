from selenium import webdriver

# Open the browser and start the innings
driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com")  # Opening shot!

# Consolidate the setup — Window control
driver.maximize_window()
driver.set_window_size(1200, 800)
driver.minimize_window()
driver.fullscreen_window()

# Read the pitch — Page info
print("Title:", driver.title)
print("Current URL:", driver.current_url)
print("Page Source length:", len(driver.page_source))

# Rotate the strike — Navigation
driver.refresh()
driver.back()
driver.forward()

# Finish strong — Wrap up the browser session
driver.close()   # Ends the tab, like taking a single
driver.quit()    # Full stop — innings closed
