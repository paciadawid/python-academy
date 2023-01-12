from ui_tests.pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


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
