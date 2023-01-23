import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.common import NoSuchElementException, TimeoutException
from ui_tests.pages.base import BasePage


class LoginPage(BasePage):
    login_tab_selector = (By.CSS_SELECTOR, "[href='/login']")
    email_field_selector = (By.XPATH, "//input[@data-qa='login-email']")
    password_field_selector = (By.XPATH, "//input[@data-qa='login-password']")
    login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")
    logged_user_selector = (By.CSS_SELECTOR, ".fa-user")

    def login_using_email_password(self, email, password):
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        time.sleep(3)
        self.driver.find_element(*self.login_button_selector).click()

    def check_if_logged_in(self):
        try:
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.logged_user_selector))
        except TimeoutException:
            return False