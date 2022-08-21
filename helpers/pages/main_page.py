from selenium.webdriver.common.by import By

from helpers.pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная страница PageObject: https:https://www.w3schools.com.
    """

    path = '/'

    TUTORIALS = (By.CSS_SELECTOR, ".w3-bar.w3-card-2 > .w3-bar-item:nth-child(2)")
    LEARN_SQL = (By.CSS_SELECTOR, "#nav_tutorials .w3-col.l3.m6:nth-child(4) > .w3-button:nth-child(2)")

    def go_to_tutorials(self):
        self._click(*self.TUTORIALS)

    def go_to_learn_sql(self):
        self.go_to_tutorials()
        self._click(*self.LEARN_SQL)
