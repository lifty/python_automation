from appium import webdriver


class CoreTestCase:
    appPackage = 'org.wikipedia'
    APPIUM_URL = 'http://127.0.0.1:4723/wd/hub'
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "AndroidTestDevice",
        "orientation": "PORTRAIT",
        "platformVersion": "6.0",
        "automationName": "Appium",
        "appPackage": "org.wikipedia",
        "appActivity": ".main.MainActivity",
        "app": "C:/Users/Crowdsystems/Documents/GitHub/python_automation/apks/wikipedia.apk"
    }
    driver = webdriver.Remote(APPIUM_URL, desired_capabilities)

    def set_up(self):
        self.driver = webdriver.Remote(self.APPIUM_URL, self.desired_capabilities)

    def tear_down(self):
        self.driver.quit()

    def rotate_screen_pt(self):
        self.driver.orientation = "PORTRAIT"

    def rotate_screen_ls(self):
        self.driver.orientation = "LANDSCAPE"

    def background_app(self, seconds):
        self.driver.background_app(seconds)
