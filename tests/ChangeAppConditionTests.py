import pytest
from lib.CoreTestCase import CoreTestCase
from lib.ui.SearchPageObject import SearchPageObject


class TestChangeAppCondition(CoreTestCase):
    def test_screen_rotation(self):
        self.set_up()
        SearchPageObject.skip_first_screen(SearchPageObject(self.driver))
        SearchPageObject.init_search_input(SearchPageObject(self.driver))
        self.rotate_screen_ls()
        SearchPageObject.assert_search_field_present(SearchPageObject(self.driver))
        self.rotate_screen_pt()
        SearchPageObject.assert_search_field_present(SearchPageObject(self.driver))
        self.tear_down()

if __name__ == '__main__':
    pytest.main()
