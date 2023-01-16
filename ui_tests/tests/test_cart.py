import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.cart import CartPage
from ui_tests.pages.home import HomePage
from ui_tests.pages.login import LoginPage
from ui_tests.pages.products import ProductsPage


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get("https://automationexercise.com/")

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def test_total_cart_sum(self):
        self.home_page.close_ad_by_refresh()
        self.login_page.login_using_email_password("seleniumremote@gmail.com", "tester")
        self.products_page.add_product_to_cart("Men tshirt")
        self.products_page.add_product_to_cart("Unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
