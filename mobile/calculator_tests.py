import unittest

from mobile.helpers import create_driver
from mobile.screens.home import HomePage


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = create_driver("Android", "calculator.apk")
        self.home_page = HomePage(self.driver)

    def test_something(self):
        self.home_page.add_values(3, 5)
        self.assertEqual(self.home_page.get_result(), 8)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
