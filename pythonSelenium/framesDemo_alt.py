# A new file named framesDemo_alt.py has been created. It demonstrates several ways to work with frames using Selenium on https://rahulshettyacademy.com/AutomationPractice/:

# Switching to a frame by name and interacting with elements inside.
# Switching to a frame by index.
# Listing all frames on the page and printing their ids/names.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Setup Chrome driver (update path as needed)
service_obj = Service("C:/Users/kneumova/Documents/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Example 1: Switch to single frame by name and interact
# The frame on this page has name 'iframe-name' and id 'courses-iframe'
driver.switch_to.frame("courses-iframe")
print("Inside frame title:", driver.title)
# Interact with an element inside the frame (e.g., click a visible link)
try:
    driver.find_element(By.LINK_TEXT, "Home").click()
    print("Clicked 'Home' link inside frame.")
except Exception as e:
    print("Could not click 'Home' link:", e)
# Switch back to main content
driver.switch_to.default_content()

# Example 2: Switch to frame by index
frames = driver.find_elements(By.TAG_NAME, "iframe")
if frames:
    driver.switch_to.frame(0)
    print("Switched to first frame by index.")
    driver.switch_to.default_content()

# Example 3: List all frames and print their ids/names
print("All frames on the page:")
for idx, frame in enumerate(frames):
    print(f"Frame {idx}: id={frame.get_attribute('id')}, name={frame.get_attribute('name')}")

time.sleep(2)
driver.quit()
