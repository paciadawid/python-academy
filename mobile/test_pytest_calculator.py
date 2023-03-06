import allure

from mobile.helpers import create_driver
from mobile.screens.home import HomePage


def test_add_digits():
    driver = create_driver("Android", "calculator.apk")
    home_page = HomePage(driver)
    home_page.add_values(3, 123, 5)
    assert home_page.get_result() == 131

    allure.attach.file(
        driver.save_screenshot("post_assertion_screenshot.png"),
        attachment_type=allure.attachment_type.PNG,
    )
    driver.quit()
