from selenium import webdriver

class BasePage:

    timeout = 10

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
