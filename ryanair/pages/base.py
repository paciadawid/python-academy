from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    timeout = 10

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click(self, selector):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(selector)).click()

    def fill_input(self, selector, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(selector))
        element.clear()
        element.send_keys(text)

    def parse_dynamic_selector(self, selector, new_value):
        new_selector = (selector[0], selector[1].format(argument=new_value))
        return new_selector
