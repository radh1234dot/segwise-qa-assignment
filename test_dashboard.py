from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome browser
driver = webdriver.Chrome()

# 1. Open the login page
driver.get("https://ua.segwise.ai/qa_assignment")
driver.maximize_window()

# 2. Fill in login details
driver.find_element(By.NAME, "email").send_keys("qa@segwise.ai")
driver.find_element(By.NAME, "password").send_keys("segwise_test")
driver.find_element(By.NAME, "password").submit()

# Wait for the page to load
time.sleep(5)  # simple wait (you can also use WebDriverWait if needed)

# 3. Check for a metric/chart on the dashboard
try:
    metric = driver.find_element(By.XPATH, "//*[contains(text(), 'ROAS')]")
    print("✅ Login successful. Dashboard loaded. ROAS found.")
except:
    print("❌ ROAS not found. Dashboard may not have loaded correctly.")

# Close the browser
driver.quit()
