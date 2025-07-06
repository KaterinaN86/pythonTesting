# Selenium Examples: Diverse Usage Demonstrations
# Author: Example User
# This script demonstrates a variety of Selenium use cases, inspired by the provided context files.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# Setup Chrome driver (update path as needed)
service_obj = Service("C:/Users/kneumova/Documents/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.maximize_window()

# 1. Basic navigation and screenshot (using a different site)
driver.get("https://www.wikipedia.org/")
driver.save_screenshot("wikipedia_home.png")

# 2. Locating elements by different strategies
search_input = driver.find_element(By.ID, "searchInput")
search_input.send_keys("Selenium (software)")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# 3. Waiting for an element to be present (Explicit Wait)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
print("Page heading:", driver.find_element(By.ID, "firstHeading").text)

# 4. Interacting with buttons and links
content_links = driver.find_elements(By.CSS_SELECTOR, "#bodyContent a")
if content_links:
    print("First content link:", content_links[0].text)

# 5. Handling alerts (using a demo alert site)
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "alertButton").click()
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

# 6. ActionChains: Hover and click (using a different demo site)
driver.get("https://demoqa.com/menu")
action = ActionChains(driver)
menu_item = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
action.move_to_element(menu_item).perform()
time.sleep(1)
sub_item = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
action.move_to_element(sub_item).perform()

# 7. Table data extraction (using a different table site)
driver.get("https://www.w3schools.com/html/html_tables.asp")
table = driver.find_element(By.ID, "customers")
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows[1:]:
    cols = row.find_elements(By.TAG_NAME, "td")
    if cols:
        print("Company:", cols[0].text, "| Contact:", cols[1].text)

# 8. Form filling and submission (using a different form site)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.find_element(By.NAME, "firstname").send_keys("Test")
driver.find_element(By.NAME, "lastname").send_keys("User")
driver.find_element(By.ID, "sex-0").click()
driver.find_element(By.ID, "exp-2").click()
driver.find_element(By.ID, "datepicker").send_keys("06/07/2025")
driver.find_element(By.ID, "profession-1").click()
# Don't submit to avoid spam

# 9. Handling multiple windows/tabs (using a different site)
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open")
driver.switch_to.frame("iframeResult")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
all_windows = driver.window_handles
if len(all_windows) > 1:
    driver.switch_to.window(all_windows[1])
    print("New window title:", driver.title)
    driver.close()
    driver.switch_to.window(all_windows[0])

# 10. Clean up
driver.quit()
