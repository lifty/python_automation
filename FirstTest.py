import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from lib.CoreTestCase import CoreTestCase
from lib.ui.MainPageObject import MainPageObject
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common import by
import time


class TestFirstTest(CoreTestCase):

    def testSearchFieldIncludesText(self):
        self.setUp()
        MainPageObject.waitForElementAndClick(MainPageObject(),
                                              By.XPATH, "//*[contains(@text,'Skip')]", "Cannot find Skip button", 5)
        MainPageObject.assertElementHasText(MainPageObject(),
                                            By.XPATH, "//*[@class='android.widget.TextView' and @resource-id='']",
                                            "Search Wikipedia", "The element does not contain expected text value", 5)
        self.tearDown()

    # def testFindArticlesAndCancelSearch(self):
    #     self.setUp()
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[contains(@text,'Skip')]", "Cannot find Skip button", 5)
    #     self.waitForElementAndClick(
    #         By.ID, "org.wikipedia:id/search_container", "Cannot find 'Search Wikipedia' input", 5)
    #     self.waitForElementAndSendKeys(
    #         By.XPATH, "//*[contains(@text,'Search Wikipedia')]", "Cannot find Search field element", 5, "Java")
    #     element_sum_before = len(self.driver.find_elements(By.ID, "org.wikipedia:id/page_list_item_title"))
    #     assert element_sum_before > 1,\
    #         "The number of articles is " + element_sum_before + ", we are expecting at least several elements"
    #     self.waitForElementAndClear(By.ID, "org.wikipedia:id/search_src_text", "Cannot clear the element", 5)
    #     self.waitForElementNotPresent(
    #         By.ID, "org.wikipedia:id/page_list_item_title", "The element is still on the screen", 5)
    #     element_sum_after = len(self.driver.find_elements(By.ID, "org.wikipedia:id/page_list_item_title"))
    #     element_sum_expected = 0
    #     assert element_sum_after == element_sum_expected,\
    #         "The number of articles is " + element_sum_after + ", expected " + element_sum_expected
    #     self.tearDown()
    #
    # def testCheckWordInSearchResults(self):
    #     self.setUp()
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[contains(@text,'Skip')]",
    #         "Cannot find Skip button", 5)
    #     self.waitForElementAndClick(
    #         By.ID, "org.wikipedia:id/search_container",
    #         "Cannot find 'Search Wikipedia' input", 5)
    #     input_key = "Java"
    #     self.waitForElementAndSendKeys(
    #         By.XPATH, "//*[contains(@text,'Search Wikipedia')]",
    #         "Cannot find Search field element", 5, input_key)
    #     self.waitForElementPresent(
    #         By.XPATH, "//*[@class='android.view.ViewGroup' and @clickable='true']",
    #         "Cannot find at least one article", 5)
    #     element_groups = self.driver.find_elements(
    #         By.XPATH, "//*[@class='android.view.ViewGroup' and @clickable='true']")
    #     element_sum = len(element_groups)
    #     assert len(element_groups) > 0,\
    #         "The number of articles is " + str(element_sum) + ", we are expecting at least 1"
    #     iteration = 0
    #     for i in element_groups:
    #         create_xpath = str("//*[@class='android.view.ViewGroup' and @clickable='true' and @index=") \
    #                     + str(iteration) + "]//*[contains(@text, '" + input_key + "')]"
    #         self.waitForElementPresent(
    #             By.XPATH, create_xpath,
    #             "Value " + input_key + " is not found in an article with index " + str(iteration), 5)
    #         iteration += 1
    #     self.tearDown()
    #
    # def testSaveTwoArticles(self):
    #     self.setUp()
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[contains(@text,'Skip')]",
    #         "Cannot find Skip button", 5)
    #     self.waitForElementAndClick(
    #         By.ID, "org.wikipedia:id/search_container",
    #         "Cannot find 'Search Wikipedia' input", 5)
    #     input_key = "Java"
    #     self.waitForElementAndSendKeys(
    #         By.XPATH, "//*[contains(@text,'Search Wikipedia')]",
    #         "Cannot find Search field element", 5, input_key)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[@text='Object-oriented programming language']",
    #         "Cannot find searched article", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//android.widget.TextView[@text='Save']",
    #         "Cannot find Save button", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']",
    #         "Cannot find Back button", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[@text='Indonesian island']",
    #         "Cannot find searched article", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//android.widget.TextView[@text='Save']",
    #         "Cannot find Save button", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']",
    #         "Cannot find Back button", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//android.widget.ImageButton[@index=0]",
    #         "Cannot find Back button", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//android.widget.FrameLayout[@content-desc='Saved']",
    #         "Cannot find Saved button", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[@resource-id='org.wikipedia:id/item_reading_list_statistical_description' and contains(@text,'2 articles')]",
    #         "Cannot find a list with 2 articles", 5)
    #     self.swipeElementToLeft(
    #         By.XPATH, "//*[@resource-id='org.wikipedia:id/page_list_item_description' and @text='Object-oriented programming language']",
    #         "Cannot find saved article")
    #     self.waitForElementNotPresent(
    #         By.XPATH, "//*[@resource-id='org.wikipedia:id/page_list_item_description' and @text='Object-oriented programming language']",
    #         "Cannot delete saved article", 5)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[@resource-id='org.wikipedia:id/page_list_item_description' and @text='Indonesian island']",
    #         "Cannot find and click the article that should stay in the list", 5)
    #     self.waitForElementPresent(
    #         By.XPATH, "//android.webkit.WebView[@content-desc='Java']//*[contains(@content-desc,'Javanese')]",
    #         "Cannot prove the article is the expected one", 15)
    #     self.tearDown()
    #
    # def testCheckArticleTitle(self):
    #     self.setUp()
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[contains(@text,'Skip')]",
    #         "Cannot find Skip button", 5)
    #     self.waitForElementAndClick(
    #         By.ID, "org.wikipedia:id/search_container",
    #         "Cannot find 'Search Wikipedia' input", 5)
    #     input_key = "Java"
    #     self.waitForElementAndSendKeys(
    #         By.XPATH, "//*[contains(@text,'Search Wikipedia')]",
    #         "Cannot find Search field element", 5, input_key)
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[@text='Object-oriented programming language']",
    #         "Cannot find searched article", 5)
    #     self.assertElementPresent(
    #         By.ID, "org.wikipedia:id/view_page_title_text",
    #         "Cannot find the title of the article")
    #     self.tearDown()
    #
    # def testScreenRotation(self):
    #     self.setUp()
    #     self.waitForElementAndClick(
    #         By.XPATH, "//*[contains(@text,'Skip')]",
    #         "Cannot find Skip button", 5)
    #     self.waitForElementAndClick(
    #         By.ID, "org.wikipedia:id/search_container",
    #         "Cannot find 'Search Wikipedia' input", 5)
    #     self.waitForElementPresent(
    #         By.XPATH, "//*[contains(@text,'Search Wikipedia')]",
    #         "Cannot find Search field element", 5)
    #     self.rotateScreenLS()
    #     self.assertElementPresentAndRerotate(
    #         By.XPATH, "//*[contains(@text,'Search Wikipedia')]",
    #         "Cannot find Search field element")
    #     self.rotateScreenPT()
    #     self.assertElementPresentAndRerotate(
    #         By.XPATH, "//*[contains(@text,'Search Wikipedia')]",
    #         "Cannot find Search field element")


#    _________________________________________________________________________________

    # def waitForElementPresent(self, by, locator, error_message, timeout_seconds):
    #     time.sleep(1)
    #     element = WebDriverWait(self.driver, timeout_seconds).until(
    #         expected_conditions.presence_of_element_located((by, locator)), error_message)
    #     return element
    #
    # def waitForElementNotPresent(self, by, locator, error_message, timeout_seconds):
    #     element = WebDriverWait(self.driver, timeout_seconds).until(
    #         expected_conditions.invisibility_of_element_located((by, locator)), error_message)
    #     return element
    #
    # def waitForElementAndClick(self, by, locator, error_message, timeout_seconds):
    #     element = self.waitForElementPresent(by, locator, error_message, timeout_seconds)
    #     element.click()
    #     return element
    #
    # def waitForElementAndSendKeys(self, by, locator, error_message, timeout_seconds, keys):
    #     element = self.waitForElementPresent(by, locator, error_message, timeout_seconds)
    #     element.send_keys(keys)
    #     self.driver.hide_keyboard()
    #     return element
    #
    # def waitForElementAndClear(self, by, locator, error_message, timeout_seconds):
    #     element = self.waitForElementPresent(by, locator, error_message, timeout_seconds)
    #     element.clear()
    #     return element
    #
    # def assertElementHasText(self, by, locator, expected_value, error_message, timeout_seconds):
    #     element = self.waitForElementPresent(by, locator, error_message, timeout_seconds)
    #     actual_value = element.get_attribute("text")
    #     assert actual_value == expected_value, error_message
    #     return element
    #
    # def getAmountOfElements(self, by, locator):
    #     elements = self.driver.find_elements(by, locator)
    #     return len(elements)
    #
    # def rotateScreenPT(self):
    #     self.driver.orientation = "PORTRAIT"
    #
    # def rotateScreenLS(self):
    #     self.driver.orientation = "LANDSCAPE"
    #
    # def assertElementPresent(self, by, locator, error_message):
    #     amount_of_elements = self.getAmountOfElements(by, locator)
    #     if amount_of_elements == 0:
    #         default_message = "An element '" + str(locator) + "' supposed to be presented"
    #         raise AssertionError(default_message + "\n" + error_message)
    #     return
    #
    # def assertElementPresentAndRerotate(self, by, locator, error_message):
    #     amount_of_elements = self.getAmountOfElements(by, locator)
    #     if amount_of_elements == 0:
    #         current_location = self.driver.orientation
    #         if str(current_location) != "PORTRAIT":
    #             self.rotateScreenPT()
    #         default_message = "An element '" + str(locator) + "' supposed to be presented"
    #         raise AssertionError(default_message + "\n" + error_message)
    #     return
    #
    # def swipeUp(self, time_of_swipe):
    #     action = TouchAction(self.driver)
    #     size = self.driver.get_window_size()
    #     x = size.width / 2
    #     start_y = size.height * 0.8
    #     end_y = size.height * 0.2
    #     action.press(x, start_y).wait(time_of_swipe).move_to(x, end_y).release().perform()
    #
    # def swipeUpQuick(self):
    #     self.swipeUp(200)
    #
    # def swipeUpToFindElement(self, by, locator, error_message, max_swipes):
    #     already_swiped = 0
    #     while self.getAmountOfElements(by, locator) == 0:
    #         if already_swiped > max_swipes:
    #             self.waitForElementPresent(by, locator, "Cannot find element by swiping up. \n" + error_message, 0)
    #             return
    #         self.swipeUpQuick()
    #         time.sleep(1)
    #         already_swiped += 1
    #
    # def swipeElementToLeft(self, by, locator, error_message):
    #     element = self.waitForElementPresent(by, locator, error_message, 10)
    #     left_x = element.location['x']
    #     right_x = left_x + element.size['width']
    #     upper_y = element.location['y']
    #     lower_y = upper_y + element.size['height']
    #     y = (upper_y + lower_y) / 2
    #     action = TouchAction(self.driver)
    #     action.press(None, right_x, y).wait(150).move_to(None, left_x, y).release().perform()
    #     time.sleep(1)

if __name__ == '__main__':
    pytest.main()
