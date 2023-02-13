from appium.webdriver.common.appiumby import AppiumBy

from mobile.screens.base import BasePage


class HomePage(BasePage):
    # static selectors
    plus_button_selector = (AppiumBy.ACCESSIBILITY_ID, "plus")
    equals_button_selector = (AppiumBy.ACCESSIBILITY_ID, "equals")
    result_field_selector = (AppiumBy.ID, "result_final")
    expand_button_selector = (AppiumBy.ACCESSIBILITY_ID, "Expand")
    sinus_button_selector = (AppiumBy.ACCESSIBILITY_ID, "sine")
    rad_deg_mode_button_selector = (AppiumBy.ID, "toggle_mode")
    pi_button_selector = (AppiumBy.ACCESSIBILITY_ID, "pi")

    # dynamic selectors
    digit_button_selector = (AppiumBy.ID, "digit_{argument}")

    def add_values(self, x, y):
        self.click(self.parse_dynamic_selector(self.digit_button_selector, x))
        self.click(self.plus_button_selector)
        self.click(self.parse_dynamic_selector(self.digit_button_selector, y))
        self.click(self.equals_button_selector)

    def get_result(self):
        return float(self.driver.find_element(*self.result_field_selector).text)

    def calculate_sinus(self, value, mode="DEG"):
        self.click(self.expand_button_selector)
        self.click(self.sinus_button_selector)

        element = self.driver.find_element(*self.rad_deg_mode_button_selector)
        if element.text == mode:
            element.click()

        if value == "pi":
            self.click(self.pi_button_selector)
        elif value == "e":
            pass
        else:
            self.click(self.parse_dynamic_selector(self.digit_button_selector, value))

        self.click(self.equals_button_selector)
