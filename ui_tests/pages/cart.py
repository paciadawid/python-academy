from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from ui_tests.pages.base import BasePage


class CartPage(BasePage):
    cart_tab_selector = (By.XPATH, "//a[@href='/view_cart']")
    checkout_button_selector = (By.CLASS_NAME, "check_out")
    empty_cart_selector = (By.ID, "empty_cart")

    def navigate_to_cart(self):
        self.driver.find_element(*self.cart_tab_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button_selector).click()

    def check_if_empty_cart(self):
        try:
            return self.driver.find_element(*self.empty_cart_selector)
        except NoSuchElementException:
            return False
