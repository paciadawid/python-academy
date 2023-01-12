class BasePage:

    timeout = 10

    def __init__(self, driver):
        self.driver = driver
