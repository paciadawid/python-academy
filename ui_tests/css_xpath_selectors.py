from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://automationexercise.com/")

driver.find_element(By.CSS_SELECTOR, ".logo img")
driver.find_element(By.CSS_SELECTOR, ".shop-menu [href='/view_cart']")
driver.find_element(By.CSS_SELECTOR, "#susbscribe_email")
driver.find_element(By.CSS_SELECTOR, ".right.control-carousel")
driver.find_element(By.CSS_SELECTOR, ".brands_products  > h2")
driver.find_element(By.CSS_SELECTOR, "footer")

driver.find_element(By.XPATH, "//a[@href='/']/img")
driver.find_element(By.XPATH, "//li/a[@href='/view_cart']")
driver.find_element(By.XPATH, "//input[@id='susbscribe_email']")
driver.find_element(By.XPATH, "//*[@href='#slider-carousel' and @data-slide='next']")
driver.find_element(By.XPATH, "//div[@class='brands_products']/h2")
driver.find_element(By.XPATH, "//footer")
