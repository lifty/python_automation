from selenium.webdriver.common.by import By
from lib.ui.MainPageObject import MainPageObject


class SearchPageObject(MainPageObject):
    def __init__(self, driver):
        super().__init__(driver)

    SKIP_ELEMENT = "//*[contains(@text,'Skip')]"
    SEARCH_INIT_ELEMENT = "org.wikipedia:id/search_container"
    SEARCH_INPUT = "//*[contains(@text,'Search Wikipedia')]"
    SEARCH_CANCEL_BUTTON = "org.wikipedia:id/search_close_btn"
    SEARCH_IS_EMPTY = "org.wikipedia:id/search_empty_container"
    BACK_BUTTON = "//android.widget.ImageButton[@index=0]"
    SEARCH_RESULT_BY_TITLE_AND_DESC_TPL = "//*[@class='android.view.ViewGroup' and @index={i}]//*[@resource-id='org.wikipedia:id/page_list_item_title' and contains(@text,'{TITLE}')]/..//*[@resource-id='org.wikipedia:id/page_list_item_description' and contains(@text,'{DESCRIPTION}')]"
    SEARCH_RESULT_BY_SUBSTRING_TPL = "//*[@resource-id='org.wikipedia:id/search_results_list']//*[contains(@text,'{SUBSTRING}')]"
    SEARCH_RESULT_TITLE_ELEMENT = "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@resource-id='org.wikipedia:id/page_list_item_title']"

    # TEMPLATES METHODS
    def __get_result_search_element(self, substring):
        return self.SEARCH_RESULT_BY_SUBSTRING_TPL.replace("{SUBSTRING}", substring)

    def __get_result_search_by_title_and_description_element(self, i, title, desc):
        index_replaced = self.SEARCH_RESULT_BY_TITLE_AND_DESC_TPL.replace("{i}", i)
        title_replaced = index_replaced.replace("{TITLE}", title)
        return title_replaced.replace("{DESCRIPTION}", desc)
    # TEMPLATES METHODS

    def skip_first_screen(self):
        self.wait_for_element_and_click(By.XPATH, self.SKIP_ELEMENT, "Cannot find Skip button", 5)
        return

    def init_search_input(self):
        self.wait_for_element_present(By.ID, self.SEARCH_INIT_ELEMENT, "Cannot find search input", 5)
        self.wait_for_element_and_click(By.ID, self.SEARCH_INIT_ELEMENT, "Cannot find and click search init element", 5)
        return

    def type_search_line(self, search_line):
        self.wait_for_element_and_send_keys(By.XPATH, self.SEARCH_INPUT,
                                            "Cannot find Search field element", 5, search_line)
        return

    def wait_for_search_result(self, substring):
        search_result_xpath = self.__get_result_search_element(substring)
        self.wait_for_element_present(By.XPATH, search_result_xpath,
                                      "Cannot find search result with substring " + substring, 5)
        return

    def click_by_article_with_substring(self, substring):
        search_result_xpath = self.__get_result_search_element(substring)
        self.wait_for_element_and_click(By.XPATH, search_result_xpath,
                                        "Cannot find search result with substring " + substring, 10)
        return

    def wait_for_element_by_title_and_description(self, title, desc, element_sum_to_check):
        self.type_search_line(title + " " + desc)
        self.assert_article_amount_gt(element_sum_to_check)
        i = 0
        while i < element_sum_to_check:
            search_result_xpath = self.__get_result_search_by_title_and_description_element(str(i), title, desc)
            self.wait_for_element_present(By.XPATH, search_result_xpath,
                                          "Cannot find search result with title " + title + " and description " + desc + " by xpath " + search_result_xpath, 5)
            i += 1
        return

    def check_article_includes_search_line(self, element_sum, search_line):
        for i in element_sum:
            create_xpath = "//*[@class='android.view.ViewGroup' and @index=" + i + "]//*[contains(@text, '" + search_line + "')]"
            self.wait_for_element_present(By.XPATH, create_xpath,
                                          "Value " + search_line + " is not found in an article with index " + i, 5)
            i += 1
        return

    def wait_and_click_search_cancel(self):
        self.wait_for_element_and_click(By.ID, self.SEARCH_CANCEL_BUTTON,
                                        "Cannot find search cancel button to click", 5)
        self.wait_for_element_present(By.ID, self.SEARCH_IS_EMPTY, "Search empty container is not presented", 5)
        return

    def leave_search(self):
        self.wait_for_element_and_click(By.XPATH, self.BACK_BUTTON, "Cannot find Back button", 5)
        return

    def get_amount_of_found_articles(self):
        self.wait_for_element_present(By.XPATH, self.SEARCH_RESULT_TITLE_ELEMENT, "Cannot find any search result", 5)
        return self.get_amount_of_elements(By.XPATH, self.SEARCH_RESULT_TITLE_ELEMENT)

    def wait_for_empty_result(self):
        self.wait_for_element_not_present(By.ID, self.SEARCH_RESULT_TITLE_ELEMENT,
                                          "The search result is still presented", 5)
        return

    def assert_there_is_no_search_result(self):
        self.assert_element_not_present(By.XPATH, self.SEARCH_RESULT_TITLE_ELEMENT,
                                        "Search result supposed not to be presented")
        return

    def assert_article_amount_gt(self, gt):
        element_sum = self.get_amount_of_found_articles()
        compare_counted_elements = element_sum > gt
        assert compare_counted_elements,\
            "The number of articles is " + element_sum + ", we are expecting at least " + (gt + 1)
        return element_sum

    def assert_search_field_present(self):
        self.assert_element_present(By.ID, self.SEARCH_INIT_ELEMENT, "Cannot find 'Search Wikipedia' input")
        return

    def assert_search_field_has_text(self):
        self.assert_element_has_text(By.XPATH, "//*[@class='android.widget.TextView' and @resource-id='']",
                                     "Search Wikipedia", "The element does not contain expected text value", 5)
        return
