import unittest

from mobile.helpers import create_driver
from mobile.screens.search import SearchPage


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver("Android", "ryanair.apk")
        self.search_page = SearchPage(self.driver)

    def test_search_flight(self):
        self.search_page.start_search()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
