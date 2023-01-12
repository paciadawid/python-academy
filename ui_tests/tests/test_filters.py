import unittest
from random import choice

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.home import HomePage
from ui_tests.pages.login import LoginPage


class MyTestCase(unittest.TestCase):
    product_tab_selector = (By.XPATH, "//a[@href='/products']")
    search_product_input_selector = (By.ID, "search_product")
    category_tab_selector = (By.CSS_SELECTOR, ".panel-title > a")
    subcategory_tab_selector = (By.CSS_SELECTOR, ".panel-collapse.in a")
    product_item_selector = (By.CLASS_NAME, "single-products")
    brand_tab_selector = (By.CSS_SELECTOR, ".brands-name a")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get("https://automationexercise.com/")

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

        self.home_page.close_ad_by_refresh()
        self.login_page.login_using_email_password("seleniumremote@gmail.com", "tester")

    def test_category(self):
        categories = self.driver.find_elements(*self.category_tab_selector)
        chosen_category = choice(categories)

        chosen_category.click()
        subcategories = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.subcategory_tab_selector))
        chosen_subcategory = choice(subcategories)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(chosen_subcategory)).click()

        products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.product_item_selector))
        self.assertGreater(len(products), 0)

    def test_brands(self):
        brands = self.driver.find_elements(*self.brand_tab_selector)
        chosen_brand = choice(brands)
        number_of_items = int(chosen_brand.text.split("\n")[0][1:-1])
        chosen_brand.click()
        products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.product_item_selector))
        self.assertEqual(number_of_items, len(products))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
