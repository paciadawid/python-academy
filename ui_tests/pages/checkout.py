from selenium.webdriver.common.by import By

from ui_tests.pages.base import BasePage


class CheckoutPage(BasePage):
    cart_total_price_selector = (By.CLASS_NAME, "cart_total_price")

    def get_items_prices(self):
        prices_elements = self.driver.find_elements(*self.cart_total_price_selector)
        prices_elements[:-1]

    def get_total_amount(self):
        prices_elements = self.driver.find_elements(*self.cart_total_price_selector)
        prices_elements[-1]
