import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.home import HomePage
from ui_tests.pages.login import LoginPage


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get("https://automationexercise.com/")

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

        self.home_page.close_ad_by_refresh()
        self.login_page.login_using_email_password("seleniumremote@gmail.com", "tester")

    def test_category(self):
        self.home_page.select_random_category()
        self.home_page.select_random_subcategory()
        self.assertGreater(len(self.home_page.get_visible_products()), 0)

    def test_brands(self):
        number_of_items = self.home_page.select_random_brand()
        products = self.home_page.get_visible_products()
        self.assertEqual(len(products), number_of_items)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
