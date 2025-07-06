from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Use a different practice site: https://demoqa.com/buttons
service_obj = Service("C:/Users/kneumova/Documents/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://demoqa.com/buttons")
action = ActionChains(driver)

# Double click example
btn_double = driver.find_element(By.ID, "doubleClickBtn")
action.double_click(btn_double).perform()
time.sleep(1)

# Right click example
btn_right = driver.find_element(By.ID, "rightClickBtn")
action.context_click(btn_right).perform()
time.sleep(1)

# Single click example (using xpath for the third button)
btn_click = driver.find_element(By.XPATH, "//button[text()='Click Me']")
action.click(btn_click).perform()
time.sleep(1)

# Example: Input text in a text box using both send_keys and ActionChains
# Navigate to a page with a text box

driver.get("https://demoqa.com/text-box")

# Locate the text box
text_box = driver.find_element(By.ID, "userName")

# Input text using send_keys
text_box.send_keys("Selenium Test User")
time.sleep(1)

# Clear and input text using ActionChains
text_box.clear()
action.click(text_box).send_keys("ActionChains User").perform()
time.sleep(1)

# Optionally, submit the form using ActionChains
submit_btn = driver.find_element(By.ID, "submit")
action.move_to_element(submit_btn).click().perform()
time.sleep(1)

driver.quit()
