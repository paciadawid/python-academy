from appium.webdriver.common.appiumby import AppiumBy

from mobile.screens.base import BasePage


class HomePage(BasePage):
    # static selectors
    plus_button_selector = (AppiumBy.ACCESSIBILITY_ID, "plus")
    equals_button_selector = (AppiumBy.ACCESSIBILITY_ID, "equals")
    result_field_selector = (AppiumBy.ID, "result_final")

    # dynamic selectors
    digit_button_selector = (AppiumBy.ID, "digit_{argument}")

    def add_values(self, x, y):
        self.click(self.parse_dynamic_selector(self.digit_button_selector, x))
        self.click(self.plus_button_selector)
        self.click(self.parse_dynamic_selector(self.digit_button_selector, y))
        self.click(self.equals_button_selector)

    def get_result(self):
        return float(self.driver.find_element(*self.result_field_selector).text)
