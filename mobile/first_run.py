import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

app_name = "ryanair.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['app'] = app_path
desired_caps['autoGrantPermissions'] = True
desired_caps['newCommandTimeout'] = 300

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element(AppiumBy.ID, "btn_where_to_fly").click()
driver.find_element(AppiumBy.ID, "btn_where_to_fly").click()
