import pytest
from appium import webdriver

class TestFirstTest:
    def setUp(self):
        desired_capabilities = {
            "platformName": "Android",
            "deviceName": "AndroidTestDevice",
            "platformVersion": "6.0",
            "automationName": "Appium",
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity",
            "app": "C:/Users/Crowdsystems/Documents/GitHub/python_automation/apks/wikipedia.apk"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)

    def testFirstTest(self):
        self.setUp()
        print("First test run")
        self.tearDown()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()
