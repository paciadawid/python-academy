import unittest
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:

        # Returns abs path relative to this file and not cwd
        app_name = "calculator.apk"
        app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['app'] = app_path
        # ["fullReset"] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_something(self):

        digit_selector = "digit_{value}"

        self.driver.find_element(AppiumBy.ID, digit_selector.format(value=5)).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"plus").click()
        self.driver.find_element(AppiumBy.ID, digit_selector.format(value=3)).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals").click()
        result = self.driver.find_element(AppiumBy.ID, "result_final").text
        self.assertEqual(int(result), 5+3)



if __name__ == '__main__':
    unittest.main()
