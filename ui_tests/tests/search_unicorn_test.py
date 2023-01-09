import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class UnicornTestSearch(unittest.TestCase):

    product_tab_selector = (By.XPATH, "//a[@href='/products']")
    search_product_input_selector = (By.ID, "search_product")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get("https://automationexercise.com/")
        self.driver.find_element(*self.product_tab_selector).click()
        try:
            WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(self.search_product_input_selector))
        except (NoSuchElementException, TimeoutException):
            self.driver.refresh()

    def test_unicorn_search(self):
        self.driver.find_element(self.product_tab_selector).click()
        self.driver.find_element(By.ID, "search_product").send_keys("unicorn")
        self.driver.find_element(By.ID, "submit_search").click()
        products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "single-products")))
        self.assertGreaterEqual(len(products), 2)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
