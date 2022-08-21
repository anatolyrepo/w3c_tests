import pytest

from configs.config import Config
from pages.main_page import MainPage
from pages.sql_page import SqlPage
from suite.base import BaseUiTestClass


@pytest.mark.main_page
class TestMainPage(BaseUiTestClass):

    def test_go_to_sql_tutorial_page_success(self):
        """Успешный переход на страницу SQL Tutorial."""

        main_page = self.get_page(MainPage)
        main_page.go_to_learn_sql()
        self.assertions.is_equal(Config.base_url + SqlPage.path, self.browser.current_url)
