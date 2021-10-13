import pytest
from lib.CoreTestCase import CoreTestCase
from lib.ui.SearchPageObject import SearchPageObject


class TestSearch(CoreTestCase):
    def test_search_field_includes_text(self):
        self.set_up()
        SearchPageObject.skip_first_screen(SearchPageObject(self.driver))
        SearchPageObject.assert_search_field_has_text(SearchPageObject(self.driver))
        self.tear_down()

    def test_find_articles_and_cancel_search(self):
        search_line = "Java"

        self.set_up()
        SearchPageObject.skip_first_screen(SearchPageObject(self.driver))
        SearchPageObject.init_search_input(SearchPageObject(self.driver))
        SearchPageObject.type_search_line(SearchPageObject(self.driver), search_line)
        SearchPageObject.assert_article_amount_gt(SearchPageObject(self.driver), 1)
        SearchPageObject.wait_and_click_search_cancel(SearchPageObject(self.driver))
        SearchPageObject.assert_there_is_no_search_result(SearchPageObject(self.driver))
        self.tear_down()

    def test_check_word_in_search_results(self):
        search_line = "Java"

        self.set_up()
        SearchPageObject.skip_first_screen(SearchPageObject(self.driver))
        SearchPageObject.init_search_input(SearchPageObject(self.driver))
        SearchPageObject.type_search_line(SearchPageObject(self.driver), search_line)
        SearchPageObject.wait_for_search_result(SearchPageObject(self.driver), search_line)
        SearchPageObject.assert_article_amount_gt(SearchPageObject(self.driver), 1)
        SearchPageObject.wait_and_click_search_cancel(SearchPageObject(self.driver))
        SearchPageObject.wait_for_empty_result(SearchPageObject(self.driver))
        SearchPageObject.assert_there_is_no_search_result(SearchPageObject(self.driver))
        self.tear_down()

    def test_find_article_with_title_and_description(self):
        title = "Java"
        description = "program"

        self.set_up()
        SearchPageObject.skip_first_screen(SearchPageObject(self.driver))
        SearchPageObject.init_search_input(SearchPageObject(self.driver))
        SearchPageObject.wait_for_element_by_title_and_description(SearchPageObject(self.driver), title, description, 3)
        self.tear_down()

if __name__ == '__main__':
    pytest.main()
