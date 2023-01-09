from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://automationexercise.com/")

driver.find_element(By.CSS_SELECTOR, "[href='/login']").click()
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("seleniumremote@gmail.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("tester")
driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-user")))

driver.quit()