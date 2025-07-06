import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/kneumova/Documents/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

# Using a different testing site: https://the-internet.herokuapp.com/dynamic_controls
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# Click the Remove button to remove the checkbox
driver.find_element(By.CSS_SELECTOR, "#checkbox-example button").click()

# Wait for the message that confirms removal
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.ID, "message")))
print(driver.find_element(By.ID, "message").text)

# Click the Add button to add the checkbox back
driver.find_element(By.CSS_SELECTOR, "#checkbox-example button").click()

# Wait for the checkbox to reappear
wait.until(expected_conditions.presence_of_element_located((By.ID, "checkbox")))
print("Checkbox is present again.")

# Enable the input field
driver.find_element(By.CSS_SELECTOR, "#input-example button").click()

# Wait for the input field to be enabled
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input")))
driver.find_element(By.CSS_SELECTOR, "#input-example input").send_keys("Selenium Test")
print("Input field enabled and text entered.")

driver.quit()