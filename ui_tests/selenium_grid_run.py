from selenium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {"browserName": "firefox"}

driver = webdriver.Remote("http://192.168.1.28:4444", desired_capabilities=desired_capabilities)

driver.get("https://automationexercise.com/")
driver.find_element(By.ID, "header")

products = driver.find_elements(By.CSS_SELECTOR, ".single-products")
print(products)

driver.quit()
