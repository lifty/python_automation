import time
from lib.CoreTestCase import CoreTestCase
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction


class MainPageObject:
    # def __init__(self):
    #     self.driver = CoreTestCase.driver

    driver = CoreTestCase.driver

    def waitForElementPresent(self, by, locator, error_message, timeout_seconds):
        time.sleep(1)
        element = WebDriverWait(self.driver, timeout_seconds).until(
            expected_conditions.presence_of_element_located((by, locator)), error_message)
        return element

    def waitForElementNotPresent(self, by, locator, error_message, timeout_seconds):
        element = WebDriverWait(self.driver, timeout_seconds).until(
            expected_conditions.invisibility_of_element_located((by, locator)), error_message)
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

    def getAmountOfElements(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return len(elements)

    def rotateScreenPT(self):
        self.driver.orientation = "PORTRAIT"

    def rotateScreenLS(self):
        self.driver.orientation = "LANDSCAPE"

    def assertElementPresent(self, by, locator, error_message):
        amount_of_elements = self.getAmountOfElements(by, locator)
        if amount_of_elements == 0:
            default_message = "An element '" + str(locator) + "' supposed to be presented"
            raise AssertionError(default_message + "\n" + error_message)
        return

    def assertElementPresentAndRerotate(self, by, locator, error_message):
        amount_of_elements = self.getAmountOfElements(by, locator)
        if amount_of_elements == 0:
            current_location = self.driver.orientation
            if str(current_location) != "PORTRAIT":
                self.rotateScreenPT()
            default_message = "An element '" + str(locator) + "' supposed to be presented"
            raise AssertionError(default_message + "\n" + error_message)
        return

    def swipeUp(self, time_of_swipe):
        action = TouchAction(self.driver)
        size = self.driver.get_window_size()
        x = size.width / 2
        start_y = size.height * 0.8
        end_y = size.height * 0.2
        action.press(x, start_y).wait(time_of_swipe).move_to(x, end_y).release().perform()

    def swipeUpQuick(self):
        self.swipeUp(200)

    def swipeUpToFindElement(self, by, locator, error_message, max_swipes):
        already_swiped = 0
        while self.getAmountOfElements(by, locator) == 0:
            if already_swiped > max_swipes:
                self.waitForElementPresent(by, locator, "Cannot find element by swiping up. \n" + error_message, 0)
                return
            self.swipeUpQuick()
            time.sleep(1)
            already_swiped += 1

    def swipeElementToLeft(self, by, locator, error_message):
        element = self.waitForElementPresent(by, locator, error_message, 10)
        left_x = element.location['x']
        right_x = left_x + element.size['width']
        upper_y = element.location['y']
        lower_y = upper_y + element.size['height']
        y = (upper_y + lower_y) / 2
        action = TouchAction(self.driver)
        action.press(None, right_x, y).wait(150).move_to(None, left_x, y).release().perform()
        time.sleep(1)