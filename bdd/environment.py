from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.cart import CartPage
from ui_tests.pages.home import HomePage
from ui_tests.pages.login import LoginPage
from ui_tests.pages.products import ProductsPage


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.implicitly_wait(5)
    context.driver.get("https://automationexercise.com/")

    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.products_page = ProductsPage(context.driver)
    context.cart_page = CartPage(context.driver)

    context.home_page.close_ad_by_refresh()


def after_scenario(context, scenario):
    context.driver.quit()
