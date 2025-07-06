from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/kneumova/Documents/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get("https://www.saucedemo.com/")
# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add "Sauce Labs Backpack" to cart
products = driver.find_elements(By.CLASS_NAME, "inventory_item")
for product in products:
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    if name == "Sauce Labs Backpack":
        product.find_element(By.CLASS_NAME, "btn_inventory").click()

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Checkout
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Test")
driver.find_element(By.ID, "last-name").send_keys("User")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()

# Assert success message
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "complete-header")))
success_text = driver.find_element(By.CLASS_NAME, "complete-header").text
assert "THANK YOU FOR YOUR ORDER" in success_text

driver.quit()