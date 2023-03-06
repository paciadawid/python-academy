import random

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.base import BasePage


class HomePage(BasePage):
    product_tab_selector = (By.XPATH, "//a[@href='/products']")
    search_product_input_selector = (By.ID, "search_product")
    category_tab_selector = (By.CSS_SELECTOR, ".panel-title > a")
    subcategory_tab_selector = (By.CSS_SELECTOR, ".panel-collapse.in a")
    product_item_selector = (By.CLASS_NAME, "single-products")
    brand_tab_selector = (By.CSS_SELECTOR, ".brands-name a")

    def close_ad_by_refresh(self):
        self.driver.find_element(*self.product_tab_selector).click()
        try:
            WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(self.search_product_input_selector))
        except (NoSuchElementException, TimeoutException):
            self.driver.refresh()

    def select_random_category(self):
        categories = self.driver.find_elements(*self.category_tab_selector)
        chosen_category = random.choice(categories)
        chosen_category.click()

    def select_random_subcategory(self):
        subcategories = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_all_elements_located(self.subcategory_tab_selector)
        )
        chosen_subcategory = random.choice(subcategories)
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(chosen_subcategory)).click()

    def get_visible_products(self):
        products = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_all_elements_located(self.product_item_selector)
        )
        return products

    def select_random_brand(self):
        brands = self.driver.find_elements(*self.brand_tab_selector)
        chosen_brand = random.choice(brands)
        number_of_items = int(chosen_brand.text.split("\n")[0][1:-1])
        chosen_brand.click()
        return number_of_items
