from selenium.webdriver.common.by import By

from ryanair.pages.base import BasePage


class HomePage(BasePage):
    cookie_button_selector = (By.CLASS_NAME, "cookie-popup-with-overlay__button")
    one_way_button_selector = (By.XPATH, "//*[@data-ref='flight-search-trip-type__one-way-trip']")
    return_button_selector = (By.XPATH, "//*[@data-ref='flight-search-trip-type__return-trip']")
    departure_field_selector = (By.ID, "input-button__departure")
    destination_field_selector = (By.ID, "input-button__destination")

    # dynamic selectors
    airport_item_selector = (By.XPATH, "//*[@data-id='{argument}']")

    def close_cookies(self):
        self.click(self.cookie_button_selector)

    def select_trip_type(self, trip_type="one-way"):
        if trip_type == "one-way":
            self.click(self.one_way_button_selector)
        elif trip_type == "return":
            self.click(self.return_button_selector)
        else:
            Exception("Choose 'one-way' or 'return'")

    def select_departure_city(self, airport_code):
        self.click(self.departure_field_selector)
        self.click(self.parse_dynamic_selector(self.airport_item_selector, airport_code))

    def select_destination_city(self):
        pass

    def select_departure_date(self):
        pass

    def accept_terms_and_conditions(self):
        pass
