import pytest

from helpers.pages.sql_try_select_all import SqlSelectAllPage
from helpers.suite.base import BaseUiTestClass


@pytest.mark.sql_tests
class TestSqlSelectInsertUpdate(BaseUiTestClass):

    def test_select_all_check_address(self):
        """Вывести все строки таблицы Customers и убедиться, что запись с ContactName равной 'Giovanni Rovelli'
           имеет Address = 'Via Ludovico il Moro 22'."""
        line = 49
        select_all_page = self.get_page(SqlSelectAllPage)
        select_all_page.insert_sql_code("SELECT * FROM Customers;")
        select_all_page.run_sql()

        contact_name = select_all_page.get_contact_name_by_line_number(line)
        address = select_all_page.get_address_by_line_number(line)

        self.assertions.is_equal("Giovanni Rovelli", contact_name)
        self.assertions.is_equal("Via Ludovico il Moro 22", address)

    def test_select_all_check_line_count(self):
        """Вывести только те строки таблицы Customers, где city='London'. Проверить, что в таблице ровно 6 записей."""
        select_all_page = self.get_page(SqlSelectAllPage)
        select_all_page.insert_sql_code("SELECT * FROM Customers Where City = 'London';")
        select_all_page.run_sql()
        number_of_records = select_all_page.get_number_of_records()

        self.assertions.is_equal(number_of_records, "6")

    def test_select_all_add_row_and_check_result(self):
        """Добавить новую запись в таблицу Customers и проверить, что эта запись добавилась."""
        select_all_page = self.get_page(SqlSelectAllPage)
        select_all_page.insert_sql_code(
            "INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)  "
            "VALUES (10001, 1, 2, 3, 4, Null, Null);"
        )
        select_all_page.run_sql()
        success_result = select_all_page.get_success_result()

        self.assertions.is_equal(success_result, "You have made changes to the database. Rows affected: 1")

    # Параметризация для последующего расширения тестового покрытия
    @pytest.mark.parametrize(
        'params', [
            pytest.param(

                {
                    'CustomerName': 'Cristina',
                    'ContactName': 'Monica',
                    'Address': 'Omskaya str.',
                    'City': 'Moscow',
                    'PostalCode': '122',
                    'Country': 'Russia'
                }

            )
        ],
        ids=["6 fields update"]
    )
    def test_select_all_update_row_and_check_values(self, params):
        """Обновить все поля (кроме CustomerID) в любой записи таблицы Customers и проверить,
           что изменения записались в базу."""
        line = 1
        select_all_page = self.get_page(SqlSelectAllPage)
        select_all_page.insert_sql_code(
            f"UPDATE Customers set "
            f"CustomerName = '{params['CustomerName']}', "
            f"ContactName='{params['ContactName']}', "
            f"Address='{params['Address']}', "
            f"City='{params['City']}', "
            f"PostalCode='{params['PostalCode']}', "
            f"Country='{params['Country']}' "
            f"where CustomerID=1;"
        )
        select_all_page.run_sql()
        select_all_page.insert_sql_code("SELECT * FROM Customers;")
        select_all_page.run_sql()

        results_6_fields = [
            select_all_page.get_customer_name_by_line_number(line),
            select_all_page.get_contact_name_by_line_number(line),
            select_all_page.get_address_by_line_number(line),
            select_all_page.get_city_by_line_number(line),
            select_all_page.get_postal_code_by_line_number(line),
            select_all_page.get_country_by_line_number(line)
        ]
        # Это не софт ассерт
        for num, key in enumerate(params):
            self.assertions.is_equal(params[key], results_6_fields[num])
