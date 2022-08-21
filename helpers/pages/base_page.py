from abc import abstractmethod
from typing import List

from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    Базовый PageObject.
    """

    @property
    @abstractmethod
    def path(self):
        raise NotImplementedError

    def __init__(self, driver):
        self._driver: ChromiumDriver = driver
        self.wait = WebDriverWait(self._driver, 15)

    def _find_element(self, by, locator) -> WebElement:
        return self._driver.find_element(by, locator)

    def _find_elements(self, by, locator) -> List[WebElement]:
        return self._driver.find_elements(by, locator)

    def _click(self, by, locator):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        self._find_element(by, locator).click()

    def _send_keys(self, by, locator, text):
        self.wait.until((EC.visibility_of_element_located((by, locator))))
        self._find_element(by, locator).clear()
        self._find_element(by, locator).send_keys(text)

    def _execute_script(self, scrypt):
        self._driver.execute_script(scrypt)
