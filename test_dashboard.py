
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup browser options
options = Options()
options.add_argument('--headless')  # Run in background (no window)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Step 1: Open login page
    driver.get("https://ua.segwise.ai/qa_assignment")
    wait = WebDriverWait(driver, 10)

    # Step 2: Log in with test credentials
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = driver.find_element(By.NAME, "password")
    email_input.send_keys("qa@segwise.ai")
    password_input.send_keys("segwise_test")
    password_input.send_keys(Keys.RETURN)

    # Step 3: Wait for dashboard to load
    dashboard_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Dashboard')]"))
    )

    # Step 4: Assert presence of ROAS chart or similar metric
    roas_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'ROAS')]"))
    )

    print("test passed: Dashboard loaded and ROAS element found.")

except Exception as e:
    print("test failed: {e}")

finally:
    driver.quit()
