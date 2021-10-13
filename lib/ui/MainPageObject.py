import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction


class MainPageObject:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_present(self, by, locator, error_message, timeout_seconds):
        time.sleep(1)
        element = WebDriverWait(self.driver, timeout_seconds).until(
            expected_conditions.presence_of_element_located((by, locator)), error_message)
        return element

    def wait_for_element_not_present(self, by, locator, error_message, timeout_seconds):
        element = WebDriverWait(self.driver, timeout_seconds).until(
            expected_conditions.invisibility_of_element_located((by, locator)), error_message)
        return element

    def wait_for_element_and_click(self, by, locator, error_message, timeout_seconds):
        element = self.wait_for_element_present(by, locator, error_message, timeout_seconds)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, by, locator, error_message, timeout_seconds, keys):
        element = self.wait_for_element_present(by, locator, error_message, timeout_seconds)
        element.send_keys(keys)
        self.driver.hide_keyboard()
        return element

    def wait_for_element_and_clear(self, by, locator, error_message, timeout_seconds):
        element = self.wait_for_element_present(by, locator, error_message, timeout_seconds)
        element.clear()
        return element

    def assert_element_has_text(self, by, locator, expected_value, error_message, timeout_seconds):
        element = self.wait_for_element_present(by, locator, error_message, timeout_seconds)
        actual_value = element.get_attribute("text")
        assert actual_value == expected_value, error_message
        return element

    def get_amount_of_elements(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return len(elements)

    def assert_element_present(self, by, locator, error_message):
        amount_of_elements = self.get_amount_of_elements(by, locator)
        if amount_of_elements == 0:
            default_message = "An element '" + str(locator) + "' supposed to be presented"
            raise AssertionError(default_message + "\n" + error_message)
        return

    def assert_element_not_present(self, by, locator, error_message):
        amount_of_elements = self.get_amount_of_elements(by, locator)
        if amount_of_elements > 0:
            default_message = "An element '" + str(locator) + "' supposed not to be presented"
            raise AssertionError(default_message + "\n" + error_message)
        return

    def swipe_up(self, time_of_swipe):
        action = TouchAction(self.driver)
        size = self.driver.get_window_size()
        x = size.width / 2
        start_y = size.height * 0.8
        end_y = size.height * 0.2
        action.press(x, start_y).wait(time_of_swipe).move_to(x, end_y).release().perform()

    def swipe_up_quick(self):
        self.swipe_up(200)

    def swipe_up_to_find_element(self, by, locator, error_message, max_swipes):
        already_swiped = 0
        while self.get_amount_of_elements(by, locator) == 0:
            if already_swiped > max_swipes:
                self.wait_for_element_present(by, locator, "Cannot find element by swiping up. \n" + error_message, 0)
                return
            self.swipe_up_quick()
            time.sleep(1)
            already_swiped += 1

    def swipe_element_to_left(self, by, locator, error_message):
        element = self.wait_for_element_present(by, locator, error_message, 10)
        left_x = element.location['x']
        right_x = left_x + element.size['width']
        upper_y = element.location['y']
        lower_y = upper_y + element.size['height']
        y = (upper_y + lower_y) / 2
        action = TouchAction(self.driver)
        action.press(None, right_x, y).wait(150).move_to(None, left_x, y).release().perform()
        time.sleep(1)
