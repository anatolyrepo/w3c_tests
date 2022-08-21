from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SqlPage(BasePage):
    """
    PageObject: https://www.w3schools.com/sql/default.asp'.

    """

    path = '/sql/default.asp'

    TRY_IT_YOURSELF = (By.CSS_SELECTOR, ".w3-example > .w3-btn.w3-margin-bottom")

    def go_try_it(self):
        self._click(*self.TRY_IT_YOURSELF)
