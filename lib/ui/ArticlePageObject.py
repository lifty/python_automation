from selenium.webdriver.common.by import By
from lib.ui.MainPageObject import MainPageObject


class ArticlePageObject(MainPageObject):
    def __init__(self, driver):
        super().__init__(driver)

    TITLE = "org.wikipedia:id/view_page_title_text"
    DESCRIPTION_CONTENCE_TPL = "//*[contains(@content-desc,'{SUBSTRING}')]"
    FOOTER_ELEMENT = "//*[@text='View page in browser']"
    SAVE_BUTTON = "//android.widget.TextView[@text='Save']"
    BACK_BUTTON = "//android.widget.ImageButton[@content-desc='Navigate up']"

    # TEMPLATES METHODS
    def __get_article_contence_element(self, substring):
        return self.DESCRIPTION_CONTENCE_TPL.replace("{SUBSTRING}", substring)
    # TEMPLATES METHODS

    def wait_for_title_element(self):
        return self.wait_for_element_present(By.ID, self.TITLE, "Cannot find the title of the article", 10)

    def get_article_title(self):
        title_element = self.wait_for_title_element()
        return getattr(title_element, "text")

    def swipe_to_footer(self):
        self.swipe_up_to_find_element(By.XPATH, self.FOOTER_ELEMENT, "Cannot find the end of the article", 20)
        return

    def save_article(self):
        self.wait_for_element_and_click(By.XPATH, self.SAVE_BUTTON, "Cannot find Save button", 5)
        return

    def close_article(self):
        self.wait_for_element_and_click(By.XPATH, self.BACK_BUTTON, "Cannot find Back button", 5)
        return

    def check_article_description(self, substring):
        search_result_xpath = self.__get_article_contence_element(substring)
        self.wait_for_element_present(By.XPATH, search_result_xpath, "Cannot prove the article is the expected one", 5)
        return

    def assert_title_present(self):
        self.assert_element_present(By.ID, self.TITLE, "Cannot find the title of the article")
        return
