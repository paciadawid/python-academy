from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.base import BasePage


class ProductDetailsPage(BasePage):
    quantity_field_selector = (By.ID, "quantity")
    add_to_cart_button_selector = (By.CLASS_NAME, "cart")
    continue_shopping_button_selector = (By.CLASS_NAME, "close-modal")

    def add_to_cart(self, number_of_items):
        quantity_field = self.driver.find_element(*self.quantity_field_selector)
        quantity_field.clear()
        quantity_field.send_keys(number_of_items)
        self.driver.find_element(*self.add_to_cart_button_selector).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()
