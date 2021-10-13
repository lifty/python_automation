import pytest
from lib.CoreTestCase import CoreTestCase
from lib.ui.ArticlePageObject import ArticlePageObject
from lib.ui.MyListsPageObject import MyListsPageObject
from lib.ui.NavigationUi import NavigationUi
from lib.ui.SearchPageObject import SearchPageObject


class TestMyLists(CoreTestCase):
    def test_save_two_articles(self):
        search_line = "Java"
        first_article_desc = "Object-oriented programming language"
        second_article_desc = "Indonesian island"
        folder_desc = "2 articles"
        second_article_contence = "Javanese"

        self.set_up()
        SearchPageObject.skip_first_screen(SearchPageObject(self.driver))
        SearchPageObject.init_search_input(SearchPageObject(self.driver))
        SearchPageObject.type_search_line(SearchPageObject(self.driver), search_line)
        SearchPageObject.click_by_article_with_substring(SearchPageObject(self.driver), first_article_desc)
        ArticlePageObject.save_article(ArticlePageObject(self.driver))
        ArticlePageObject.close_article(ArticlePageObject(self.driver))
        SearchPageObject.click_by_article_with_substring(SearchPageObject(self.driver), second_article_desc)
        ArticlePageObject.save_article(ArticlePageObject(self.driver))
        ArticlePageObject.close_article(ArticlePageObject(self.driver))
        SearchPageObject.leave_search(SearchPageObject(self.driver))
        NavigationUi.click_saved_lists(NavigationUi(self.driver))
        MyListsPageObject.open_folder_by_desc(MyListsPageObject(self.driver), folder_desc)
        MyListsPageObject.swipe_article_to_delete(MyListsPageObject(self.driver), first_article_desc)
        MyListsPageObject.click_article_present_by_desc(MyListsPageObject(self.driver), second_article_desc)
        ArticlePageObject.check_article_description(ArticlePageObject(self.driver), second_article_contence)
        self.tear_down()

if __name__ == '__main__':
    pytest.main()
