import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

from configs.config import Config

manager = ChromeDriverManager()
path = manager.install()


# Передача аргументов через переменные окружения не реализована
def pytest_addoption(parser):
    parser.addoption(
        "--w3c_base_host", action="store", help="Базовый host w3c", default="www.w3schools.com",
    )


def pytest_configure(config):
    Config.configure(
        base_host=config.getoption('--w3c_base_host'),
    )


@pytest.fixture()
def browser():
    driver = Chrome(executable_path=path)
    driver.maximize_window()

    yield driver

    driver.quit()
