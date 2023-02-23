import os

from appium import webdriver


def create_driver(platform, app_name):
    # Returns abs path relative to this file and not cwd
    app_name = app_name
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

    desired_caps = {}
    desired_caps['platformName'] = platform
    desired_caps['app'] = app_path
    desired_caps['autoGrantPermissions'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver
