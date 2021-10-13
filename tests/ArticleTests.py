import pytest
from lib.CoreTestCase import CoreTestCase
from lib.ui.ArticlePageObject import ArticlePageObject
from lib.ui.SearchPageObject import SearchPageObject


class TestArticle(CoreTestCase):
    def test_check_article_title(self):
        search_line = "Java"
        first_article_desc = "Object-oriented programming language"

        self.set_up()
        SearchPageObject.skip_first_screen(SearchPageObject(self.driver))
        SearchPageObject.init_search_input(SearchPageObject(self.driver))
        SearchPageObject.type_search_line(SearchPageObject(self.driver), search_line)
        SearchPageObject.click_by_article_with_substring(SearchPageObject(self.driver), first_article_desc)
        ArticlePageObject.assert_title_present(ArticlePageObject(self.driver))
        self.tear_down()

if __name__ == '__main__':
    pytest.main()
