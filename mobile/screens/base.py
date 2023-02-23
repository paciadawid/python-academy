from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    timeout = 10

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def parse_dynamic_selector(self, selector, new_value):
        new_selector = (selector[0], selector[1].format(argument=new_value))
        return new_selector

    def click(self, selector):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(selector)).click()

    def check_if_visible(self, selector):
        try:
            return WebDriverWait(self.driver, 0.5).until(EC.visibility_of_element_located(selector))
        except TimeoutException:
            return False
