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
try:
    # Wait for the page to load
    time.sleep(2)

    # Try to find and click the alert button
    alert_button = wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
    alert_button.click()

    # Wait for alert to be present and handle it
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    print("Alert text:", alert_text)
    alert.accept()
    print("Alert handled successfully")
except Exception as e:
    print(f"Alert handling failed: {e}")
    # Try alternative alert sites or skip this demo
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)
        alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        alert_button.click()
        alert = wait.until(EC.alert_is_present())
        print("Alternative alert text:", alert.text)
        alert.accept()
        print("Alternative alert handled successfully")
    except Exception as e2:
        print(f"Alternative alert also failed: {e2}")
        print("Skipping alert demo and continuing...")

# 6. ActionChains: Hover and click (using a different demo site)
print("Starting ActionChains demo...")
try:
    driver.get("https://demoqa.com/menu")
    time.sleep(2)
    action = ActionChains(driver)
    menu_item = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
    action.move_to_element(menu_item).perform()
    time.sleep(1)
    sub_item = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
    action.move_to_element(sub_item).perform()
    print("ActionChains demo completed")
except Exception as e:
    print(f"ActionChains demo failed: {e}")
    print("Skipping ActionChains demo and continuing...")

# 7. Table data extraction (using a different table site)
print("Starting table data extraction...")
try:
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    # Wait for page to load
    time.sleep(3)
    print("Page loaded, looking for table...")

    # Try multiple table selectors as backup
    table = None
    try:
        table = wait.until(EC.presence_of_element_located((By.ID, "customers")))
        print("Found table with ID 'customers'")
    except:
        try:
            table = driver.find_element(By.CSS_SELECTOR, "table")
            print("Found first table on page")
        except:
            print("No table found, trying alternative site...")
            driver.get("https://the-internet.herokuapp.com/tables")
            time.sleep(2)
            table = wait.until(EC.presence_of_element_located((By.ID, "table1")))
            print("Found table on alternative site")

    if table:
        rows = table.find_elements(By.TAG_NAME, "tr")
        print(f"Found {len(rows)} rows in table")

        # Extract data from first few rows only
        for i, row in enumerate(rows[1:4]):  # Limit to first 3 data rows
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols and len(cols) >= 2:
                print(f"Row {i+1} - First cell: {cols[0].text} | Second cell: {cols[1].text}")

    print("Table data extraction completed")
except Exception as e:
    print(f"Table extraction failed: {e}")
    print("Skipping table demo and continuing...")

# 8. Form filling and submission (using a different form site)
print("Starting form filling demo...")
try:
    driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
    time.sleep(3)

    driver.find_element(By.NAME, "firstname").send_keys("Test")
    driver.find_element(By.NAME, "lastname").send_keys("User")
    driver.find_element(By.ID, "sex-0").click()
    driver.find_element(By.ID, "exp-2").click()
    driver.find_element(By.ID, "datepicker").send_keys("06/07/2025")
    driver.find_element(By.ID, "profession-1").click()
    print("Form filling completed successfully")
    # Don't submit to avoid spam
except Exception as e:
    print(f"Form filling failed: {e}")
    print("Skipping form demo and continuing...")

# 9. Handling multiple windows/tabs (using a different site)
print("Starting window handling demo...")
try:
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open")
    time.sleep(3)
    driver.switch_to.frame("iframeResult")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    all_windows = driver.window_handles
    if len(all_windows) > 1:
        driver.switch_to.window(all_windows[1])
        print("New window title:", driver.title)
        driver.close()
        driver.switch_to.window(all_windows[0])
        print("Window handling demo completed")
    else:
        print("No new window opened")
except Exception as e:
    print(f"Window handling failed: {e}")
    print("Skipping window demo and continuing...")

# 10. Clean up
driver.quit()
