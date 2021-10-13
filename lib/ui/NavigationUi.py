from selenium.webdriver.common.by import By
from lib.ui.MainPageObject import MainPageObject


class NavigationUi(MainPageObject):
    def __init__(self, driver):
        super().__init__(driver)

    SAVED_LISTS = "//android.widget.FrameLayout[@content-desc='Saved']"
    SEARCH_FIELD = "//*[@class='android.widget.TextView' and @resource-id='']"
    SEARCH_FIELD_VALUE = "Search Wikipedia"

    def click_saved_lists(self):
        self.wait_for_element_and_click(By.XPATH, self.SAVED_LISTS, "Cannot find Saved button", 5)
        return

    def assert_search_field_has_text(self):
        self.assert_element_has_text(By.XPATH, self.SEARCH_FIELD, self.SEARCH_FIELD_VALUE,
                                     "Text in the search field does not match " + self.SEARCH_FIELD_VALUE, 5)
        return
