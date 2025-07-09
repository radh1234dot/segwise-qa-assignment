from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("https://ua.segwise.ai/qa_assignment")
driver.maximize_window()


driver.find_element(By.NAME, "email").send_keys("qa@segwise.ai")
driver.find_element(By.NAME, "password").send_keys("segwise_test")
driver.find_element(By.NAME, "password").submit()


time.sleep(5)  


try:
    metric = driver.find_element(By.XPATH, "//*[contains(text(), 'ROAS')]")
    print("Login successful. Dashboard loaded. ROAS found.")
except:
    print(" ROAS not found. Dashboard may not have loaded correctly.")


driver.quit()
