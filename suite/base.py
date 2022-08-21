import pytest
from selenium.webdriver.chromium.webdriver import ChromiumDriver

from assertions.assertions import Assertions
from configs.config import Config


class BaseUiTestClass:
    """
    Базовый сьют.
    """
    browser: ChromiumDriver
    base_url: str
    assertions: Assertions
    base_url = Config.base_url

    @pytest.fixture(autouse=True)
    def prepare(self, browser):
        self.browser: ChromiumDriver = browser
        self.assertions = Assertions()

    def get_page(self, page_class):
        self.browser.get(self.base_url + page_class.path)
        return page_class(self.browser)
