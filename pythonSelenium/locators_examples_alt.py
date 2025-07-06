from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/kneumova/Documents/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/challenging_dom")

# By tag name: Get the first button
first_button = driver.find_element(By.TAG_NAME, "button")
print("First button text:", first_button.text)

# By class name: Get the blue button
blue_button = driver.find_element(By.CLASS_NAME, "button")
print("Blue button text:", blue_button.text)

# By CSS selector: Get the red button
red_button = driver.find_element(By.CSS_SELECTOR, ".button.alert")
print("Red button text:", red_button.text)

# By XPath: Get the green button
green_button = driver.find_element(By.XPATH, "//a[@class='button success']")
print("Green button text:", green_button.text)

# By CSS selector: Get the first cell in the table
first_cell = driver.find_element(By.CSS_SELECTOR, "table tbody tr td")
print("First cell text:", first_cell.text)

# By XPath: Get the edit link in the first row
edit_link = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[last()-1]/a")
print("Edit link text:", edit_link.text)

# By link text: Get the 'delete' link in the first row
delete_link = driver.find_element(By.LINK_TEXT, "delete")
print("Delete link text:", delete_link.text)

driver.quit()