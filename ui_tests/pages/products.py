from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.base import BasePage


class ProductsPage(BasePage):
    # cart_tab_selector = (By.CSS_SELECTOR, "//a[href='/view_cart'")
    product_tab_selector = (By.XPATH, "//a[@href='/products']")
    search_product_input_selector = (By.ID, "search_product")
    search_product_button_selector = (By.ID, "submit_search")
    product_element_selector = (By.CLASS_NAME, "single-products")
    add_to_cart_button_selector = (By.CSS_SELECTOR, ".product-overlay a")
    continue_shopping_button_selector = (By.CLASS_NAME, "btn-success")

    def search_product(self, product_name):
        self.driver.find_element(*self.product_tab_selector).click()
        product_search_input = self.driver.find_element(*self.search_product_input_selector)
        product_search_input.clear()
        product_search_input.send_keys(product_name)
        self.driver.find_element(*self.search_product_button_selector).click()

    def add_product_to_cart(self, product_name):
        self.search_product(product_name)
        product_tile = self.driver.find_element(*self.product_element_selector)
        ActionChains(self.driver).move_to_element(product_tile).perform()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.add_to_cart_button_selector)).click()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.continue_shopping_button_selector)).click()
