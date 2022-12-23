import time
from pages.test_elements_page import Tests


class Test_Smoke:

    def test_log_in(self, driver):
        test_page_main = Tests(driver, 'https://testing.coinmatics.com/')
        test_page_main.open()
        test_page_main.Log_in_user('vitals3', 'Svn_1987')
        time.sleep(3)
        expected_results = ('Dashboard - Coinmatics', 'Главная - Coinmatics', 'Cruscotto - Coinmatics')
        assert driver.title in expected_results


    def test_add_api(driver, self):
        valid_api_bybit = Tests(driver, 'https://testing.coinmatics.com/app/accounts/exchange-accounts/')
        valid_api_bybit.open()
        valid_api_bybit.Add_API_Key('auto_test_api', 'kZBf1hXDOSTnynMbZy', 'z2PwwizhMUIadPrK2y3TD1Iu4IE0qWh41agn')
        time.sleep(3)
