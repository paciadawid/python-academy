import time

from appium.webdriver.common.appiumby import AppiumBy

from mobile.screens.base import BasePage


class SearchPage(BasePage):
    search_button_selector = (AppiumBy.ID, "btn_where_to_fly")
    origin_button_selector = (AppiumBy.ID, "et_select_origin")

    def start_search(self):
        start_time = time.time()
        while True:
            self.click(self.search_button_selector)
            if self.check_if_visible(self.origin_button_selector):
                break
            if time.time() - start_time > self.timeout:
                raise TimeoutError("Element not found")
