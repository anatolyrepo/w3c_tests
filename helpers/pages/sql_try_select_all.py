from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers.pages.base_page import BasePage


class SqlSelectAllPage(BasePage):
    """
    PageObject: https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all'.

    """

    path = '/sql/trysql.asp?filename=trysql_select_all'

    RUN_SQL_BTN = (By.CSS_SELECTOR, ".ws-btn")
    CODE_MIRROR = (By.CSS_SELECTOR, "div.CodeMirror-lines")
    NUMBER_OF_RECORDS = (By.CSS_SELECTOR, ".w3-white > div:nth-child(1)  div")
    SUCCESS_RESULT = (By.CSS_SELECTOR, "#resultSQL .w3-white > div:nth-child(1)")

    INFO_ABOUT_RESTORE_DATABASE = (By.CSS_SELECTOR, "#resultSQL > .w3-white  > :nth-child(5)")

    LINE_1 = (By.CSS_SELECTOR, ".ws-table-all.notranslate tr:nth-child(2)")

    LINE_CUSTOMER_ID_NO_NUMBER = ".ws-table-all.notranslate  tr:nth-child({}) >  td:nth-child(1)"
    LINE_CUSTOMER_NAME_NO_NUMBER = ".ws-table-all.notranslate  tr:nth-child({}) >  td:nth-child(2)"
    LINE_CONTACT_NAME_NO_NUMBER = ".ws-table-all.notranslate  tr:nth-child({}) >  td:nth-child(3)"
    LINE_ADDRESS_NO_NUMBER = ".ws-table-all.notranslate  tr:nth-child({}) >  td:nth-child(4)"
    LINE_CITY_NO_NUMBER = ".ws-table-all.notranslate  tr:nth-child({}) >  td:nth-child(5)"
    LINE_POSTAL_CODE_NO_NUMBER = ".ws-table-all.notranslate  tr:nth-child({}) >  td:nth-child(6)"
    LINE_COUNTRY_NO_NUMBER = ".ws-table-all.notranslate  tr:nth-child({}) >  td:nth-child(7)"

    def run_sql(self):
        self._click(*self.RUN_SQL_BTN)
        self.wait.until_not(EC.visibility_of_element_located(self.INFO_ABOUT_RESTORE_DATABASE))

    def insert_sql_code(self, sql_code):
        self.wait.until(EC.visibility_of_element_located(self.CODE_MIRROR))
        self._execute_script(f'window.editor.getDoc().setValue("{sql_code}")')

    def get_customer_name_by_line_number(self, line_number):
        self.wait.until(EC.visibility_of_element_located(self.LINE_1))
        return self._find_element(By.CSS_SELECTOR, self.LINE_CUSTOMER_NAME_NO_NUMBER.format(line_number + 1)).text

    def get_contact_name_by_line_number(self, line_number):
        self.wait.until(EC.visibility_of_element_located(self.LINE_1))
        return self._find_element(By.CSS_SELECTOR, self.LINE_CONTACT_NAME_NO_NUMBER.format(line_number + 1)).text

    def get_address_by_line_number(self, line_number):
        self.wait.until(EC.visibility_of_element_located(self.LINE_1))
        return self._find_element(By.CSS_SELECTOR, self.LINE_ADDRESS_NO_NUMBER.format(line_number + 1)).text

    def get_city_by_line_number(self, line_number):
        self.wait.until(EC.visibility_of_element_located(self.LINE_1))
        return self._find_element(By.CSS_SELECTOR, self.LINE_CITY_NO_NUMBER.format(line_number + 1)).text

    def get_postal_code_by_line_number(self, line_number):
        self.wait.until(EC.visibility_of_element_located(self.LINE_1))
        return self._find_element(By.CSS_SELECTOR, self.LINE_POSTAL_CODE_NO_NUMBER.format(line_number + 1)).text

    def get_country_by_line_number(self, line_number):
        self.wait.until(EC.visibility_of_element_located(self.LINE_1))
        return self._find_element(By.CSS_SELECTOR, self.LINE_COUNTRY_NO_NUMBER.format(line_number + 1)).text

    def get_number_of_records(self):
        self.wait.until(EC.visibility_of_element_located(self.NUMBER_OF_RECORDS))
        return self._find_element(*self.NUMBER_OF_RECORDS).text[-1]

    def get_success_result(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_RESULT))
        return self._find_element(*self.SUCCESS_RESULT).text
