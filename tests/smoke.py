import time
from pages.test_elements_page import TestsLogInAndAddApi
from pages.test_subscribtion import TestsSubscription
from consts import URL_COINMATICS


class Test_Smoke:

    def test_log_in(self, driver):
        test_page_main = TestsLogInAndAddApi(driver, URL_COINMATICS.get('main_landing'))
        test_page_main.open()
        test_page_main.Log_in_user()
        time.sleep(5)
        expected_results = ('Dashboard - Coinmatics', 'Главная - Coinmatics', 'Cruscotto - Coinmatics')
        assert driver.title in expected_results

    def test_add_api_bybit(self, driver):
        page_exchange_accounts = TestsLogInAndAddApi(driver, URL_COINMATICS.get('exchange_accounts'))
        page_exchange_accounts.open()
        page_exchange_accounts.Add_API_Key_Bybit()
        time.sleep(5)



    def test_add_api_binance(self, driver):
        page_exchange_accounts = TestsLogInAndAddApi(driver, URL_COINMATICS.get('exchange_accounts'))
        page_exchange_accounts.open()
        page_exchange_accounts.Add_API_Key_Binance()
        time.sleep(3)

    def test_add_api_okx(self, driver):
        page_exchange_accounts = TestsLogInAndAddApi(driver, URL_COINMATICS.get('exchange_accounts'))
        page_exchange_accounts.open()
        page_exchange_accounts.Add_API_Key_OKX()
        time.sleep(61)
        driver.refresh()

    def test_subscribe_to_bybit_spot_strategy(self, driver):
        page_bybit_spot_strategy = TestsSubscription(driver, URL_COINMATICS.get('bybit_spot_strategy'))
        page_bybit_spot_strategy.open()
        page_bybit_spot_strategy.Subscribe_bybit_spot_strategy()
        expected_results = ('My subscription - Coinmatics', 'Моя подписка - Coinmatics', 'Il mio abbonamento - Coinmatics')
        assert driver.title in expected_results
