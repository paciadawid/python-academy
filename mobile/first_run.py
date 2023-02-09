import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Returns abs path relative to this file and not cwd
app_name = "calculator.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['app'] = app_path
#["fullReset"] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
