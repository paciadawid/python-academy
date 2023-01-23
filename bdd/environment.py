from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.home import HomePage
from ui_tests.pages.login import LoginPage
from ui_tests.pages.products import ProductsPage


def before_scenario(context, scenario):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.get("https://automationexercise.com/")

    context.home_page = HomePage(driver)
    context.login_page = LoginPage(driver)
    context.products_page = ProductsPage(driver)

    context.home_page.close_ad_by_refresh()
