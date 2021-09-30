import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common import by


class TestFirstTest:
    appPackage = 'org.wikipedia'

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

    def testSearchFieldIncludesText(self):
        self.setUp()
        self.waitForElementAndClick(
            By.XPATH, "//*[contains(@text,'Skip')]", "Cannot find Skip button", 5)
        self.assertElementHasText(
            By.XPATH, "//*[@class='android.widget.TextView' and @resource-id='']", "Search Wikipedia",
            "The element does not contain expected text value", 5)
        self.tearDown()

    def testFindArticlesAndCancelSearch(self):
        self.setUp()
        self.waitForElementAndClick(
            By.XPATH, "//*[contains(@text,'Skip')]", "Cannot find Skip button", 5)
        self.waitForElementAndClick(
            By.ID, "org.wikipedia:id/search_container", "Cannot find 'Search Wikipedia' input", 5)
        self.waitForElementAndSendKeys(
            By.XPATH, "//*[contains(@text,'Search Wikipedia')]", "Cannot find Search field element", 5, "Java")
        element_sum_before = len(self.driver.find_elements(By.ID, "org.wikipedia:id/page_list_item_title"))
        assert element_sum_before > 1,\
            "The number of articles is " + element_sum_before + ", we are expecting at least several elements"
        self.waitForElementAndClear(By.ID, "org.wikipedia:id/search_src_text", "Cannot clear the element", 5)
        self.waitForElementNotPresent(
            By.ID, "org.wikipedia:id/page_list_item_title", "The element is still on the screen", 5)
        element_sum_after = len(self.driver.find_elements(By.ID, "org.wikipedia:id/page_list_item_title"))
        element_sum_expected = 0
        assert element_sum_after == element_sum_expected,\
            "The number of articles is " + element_sum_after + ", expected " + element_sum_expected
        self.tearDown()

    def testCheckWordInSearchResults(self):
        self.setUp()
        self.waitForElementAndClick(
            By.XPATH, "//*[contains(@text,'Skip')]",
            "Cannot find Skip button", 5)
        self.waitForElementAndClick(
            By.ID, "org.wikipedia:id/search_container",
            "Cannot find 'Search Wikipedia' input", 5)
        input_key = "Java"
        self.waitForElementAndSendKeys(
            By.XPATH, "//*[contains(@text,'Search Wikipedia')]",
            "Cannot find Search field element", 5, input_key)
        self.waitForElementPresent(
            By.XPATH, "//*[@class='android.view.ViewGroup' and @clickable='true']",
            "Cannot find at least one article", 5)
        element_groups = self.driver.find_elements(
            By.XPATH, "//*[@class='android.view.ViewGroup' and @clickable='true']")
        element_sum = len(element_groups)
        assert len(element_groups) > 0,\
            "The number of articles is " + str(element_sum) + ", we are expecting at least 1"
        iteration = 0
        for i in element_groups:
            create_xpath = str("//*[@class='android.view.ViewGroup' and @clickable='true' and @index=") \
                        + str(iteration) + "]//*[contains(@text, '" + input_key + "')]"
            self.waitForElementPresent(
                By.XPATH, create_xpath,
                "Value " + input_key + " is not found in an article with index " + str(iteration), 5)
            iteration += 1
        self.tearDown()

    def waitForElementPresent(self, by, locator, error_message, timeout_seconds):
        time.sleep(1)
        element = WebDriverWait(self.driver, timeout_seconds).until(
            expected_conditions.presence_of_element_located((by, locator)), error_message)
        return element

    def waitForElementAndClick(self, by, locator, error_message, timeout_seconds):
        element = self.waitForElementPresent(by, locator, error_message, timeout_seconds)
        element.click()
        return element

    def waitForElementAndSendKeys(self, by, locator, error_message, timeout_seconds, keys):
        element = self.waitForElementPresent(by, locator, error_message, timeout_seconds)
        element.send_keys(keys)
        self.driver.hide_keyboard()
        return element

    def waitForElementAndClear(self, by, locator, error_message, timeout_seconds):
        element = self.waitForElementPresent(by, locator, error_message, timeout_seconds)
        element.clear()
        return element

    def assertElementHasText(self, by, locator, expected_value, error_message, timeout_seconds):
        element = self.waitForElementPresent(by, locator, error_message, timeout_seconds)
        actual_value = element.get_attribute("text")
        assert actual_value == expected_value, error_message
        return element

    def waitForElementNotPresent(self, by, locator, error_message, timeout_seconds):
        element = WebDriverWait(self.driver, timeout_seconds).until(
            expected_conditions.invisibility_of_element_located((by, locator)), error_message)
        return element

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()
