import time
from selenium.webdriver.common.by import By
from lib.ui.MainPageObject import MainPageObject


class MyListsPageObject(MainPageObject):
    def __init__(self, driver):
        super().__init__(driver)

    FOLDER_BY_DESC_TPL = "//*[@resource-id='org.wikipedia:id/item_reading_list_statistical_description' and contains(@text,'{FOLDER_DESC}')]"
    ARTICLE_BY_DESC_TPL = "//*[@resource-id='org.wikipedia:id/page_list_item_description' and @text='{ARTICLE_DESC}']"

    # TEMPLATES METHODS
    def __get_folder_xpath_by_desc(self, folder_desc):
        return self.FOLDER_BY_DESC_TPL.replace("{FOLDER_DESC}", folder_desc)

    def __get_article_xpath_by_desc(self, article_desc):
        return self.ARTICLE_BY_DESC_TPL.replace("{ARTICLE_DESC}", article_desc)
    # TEMPLATES METHODS

    def open_folder_by_desc(self, folder_desc):
        folder_desc_xpath = self.__get_folder_xpath_by_desc(folder_desc)
        self.wait_for_element_and_click(By.XPATH, folder_desc_xpath,
                                        "Cannot find folder by description " + folder_desc, 5)
        return

    def wait_for_article_present_by_desc(self, article_desc):
        article_desc_xpath = self.__get_article_xpath_by_desc(article_desc)
        self.wait_for_element_present(By.XPATH, article_desc_xpath,
                                      "Cannot find an article by description " + article_desc, 5)
        return

    def wait_for_article_not_present_by_desc(self, article_desc):
        article_desc_xpath = self.__get_article_xpath_by_desc(article_desc)
        self.wait_for_element_not_present(By.XPATH, article_desc_xpath,
                                          "Cannot find an article by description " + article_desc, 5)
        return

    def swipe_article_to_delete(self, article_desc):
        self.wait_for_article_present_by_desc(article_desc)
        article_desc_xpath = self.__get_article_xpath_by_desc(article_desc)
        self.swipe_element_to_left(By.XPATH, article_desc_xpath,
                                   "Cannot find and delete saved article by description " + article_desc)
        self.wait_for_article_not_present_by_desc(article_desc)
        time.sleep(1)
        return

    def click_article_present_by_desc(self, article_desc):
        article_desc_xpath = self.__get_article_xpath_by_desc(article_desc)
        self.wait_for_element_and_click(By.XPATH, article_desc_xpath,
                                        "Cannot find an article by description " + article_desc, 5)
        return
