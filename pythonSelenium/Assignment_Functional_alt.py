import time
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Example: Shopping cart automation on a different practice site
expectedList = ['iPhone', 'Samsung Galaxy', 'Nokia Lumia']
actualList = []

# Set Chrome options to disable password manager
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
chrome_options.add_argument("--disable-save-password-bubble")
chrome_options.add_argument("--incognito")
user_data_dir = tempfile.mkdtemp()
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')  # Use a custom profile to avoid popups

service_obj = Service("C:/Users/kneumova/Documents/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)

# Use a different demo e-commerce site
# Example: https://www.saucedemo.com/
driver.get("https://www.saucedemo.com/")
# Login (required for saucedemo)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Handle possible Chrome browser-level password update popup
try:
    # Switch to the alert and accept it if present
    WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    print("Browser password update popup appeared and was accepted.")
except:
    pass  # No browser alert appeared

# Handle possible update password popup after login
try:
    popup_ok = WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='OK' or text()='Ok' or text()='ok']"))
    )
    popup_ok.click()
    print("Password update popup appeared and was closed.")
except:
    pass  # No popup appeared

# Wait for products to be visible
products = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
)

# Select the first three products
actualList = []
for result in products[:3]:
    product_name = result.find_element(By.CLASS_NAME, "inventory_item_name").text
    actualList.append(product_name)
    # Add to cart
    add_to_cart_btn = result.find_element(By.TAG_NAME, "button")
    add_to_cart_btn.click()
    time.sleep(1)

print("Products added:", actualList)

# Go to cart
cart_btn = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_btn.click()

# Sum validation (get prices and sum them)
prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
sum = 0.0
for price in prices:
    sum += float(price.text.replace('$', ''))
print("Sum of prices:", sum)

# Clean up
driver.quit()
