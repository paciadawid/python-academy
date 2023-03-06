import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.cart import CartPage
from ui_tests.pages.home import HomePage
from ui_tests.pages.login import LoginPage
from ui_tests.pages.product_details import ProductDetailsPage
from ui_tests.pages.products import ProductsPage


def before_scenario(context, _):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument(" --disable-dev-shm-usage")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
    context.driver.implicitly_wait(5)
    context.driver.get("https://automationexercise.com/")

    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.products_page = ProductsPage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.product_details_page = ProductDetailsPage(context.driver)

    context.home_page.close_ad_by_refresh()


def after_scenario(context, scenario):
    if "failed" in str(scenario.status):
        allure.attach(
            context.driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )
    context.driver.quit()
