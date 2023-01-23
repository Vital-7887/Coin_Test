import time
from pages.test_log_in_and_add_api import TestsLogInAndAddApi
from pages.test_subscribtion import TestsSubscription
from pages.test_delete_api_key import Test_delete_api_key
from consts import URL_COINMATICS, API_BYBIT, API_OKX, API_BINANCE


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
        page_bybit_spot_strategy.Subscribe_to_strategy_with_autoalign(API_BYBIT.get('api_name'))
        expected_results = ('My subscription - Coinmatics', 'Моя подписка - Coinmatics', 'Il mio abbonamento - Coinmatics')
        assert driver.title in expected_results


    def test_subscribe_to_bybit_inverse_perpetual_strategy(self, driver):
        page_bybit_inverse_perpetual_strategy = TestsSubscription(driver, URL_COINMATICS.get('bybit_inverse_perpetual_strategy'))
        page_bybit_inverse_perpetual_strategy.open()
        page_bybit_inverse_perpetual_strategy.Subscribe_to_strategy_with_autoalign(API_BYBIT.get('api_name'))
        expected_results = ('My subscription - Coinmatics', 'Моя подписка - Coinmatics', 'Il mio abbonamento - Coinmatics')
        assert driver.title in expected_results


    def test_subscribe_to_OKX_spot_strategy(self, driver):
        page_OKX_spot_strategy = TestsSubscription(driver, URL_COINMATICS.get('OKX_spot_strategy'))
        page_OKX_spot_strategy.open()
        page_OKX_spot_strategy.Subscribe_to_strategy_with_autoalign(API_OKX.get('api_name'))
        expected_results = ('My subscription - Coinmatics', 'Моя подписка - Coinmatics', 'Il mio abbonamento - Coinmatics')
        assert driver.title in expected_results

    def test_subscribe_to_bybit_usdt_perpetual_strategy(self, driver):
        page_bybit_usdt_perpetual_strategy = TestsSubscription(driver, URL_COINMATICS.get('bybit_usdt_perpetual_strategy'))
        page_bybit_usdt_perpetual_strategy.open()
        page_bybit_usdt_perpetual_strategy.Subscribe_to_srtategy_without_autoalighn(API_BYBIT.get('api_name'))
        expected_results = ('My subscription - Coinmatics', 'Моя подписка - Coinmatics', 'Il mio abbonamento - Coinmatics')
        assert driver.title in expected_results


    def test_delete_api_bybit(self,driver):
        page_exchange_accounts = Test_delete_api_key(driver, URL_COINMATICS.get('exchange_accounts'))
        page_exchange_accounts.open()
        page_exchange_accounts.Delete_api_key(API_BYBIT.get('api_name'))
        expected_results = ('Exchange Accounts - Coinmatics', 'Биржевые аккаунты - Coinmatics', 'Account di Exchange - Coinmatics')
        assert driver.title in expected_results


    def test_delete_api_OKX(self,driver):
        page_exchange_accounts = Test_delete_api_key(driver, URL_COINMATICS.get('exchange_accounts'))
        page_exchange_accounts.open()
        page_exchange_accounts.Delete_api_key(API_OKX.get('api_name'))
        expected_results = ('Exchange Accounts - Coinmatics', 'Биржевые аккаунты - Coinmatics', 'Account di Exchange - Coinmatics')
        assert driver.title in expected_results


    def test_delete_api_binance(self,driver):
        page_exchange_accounts = Test_delete_api_key(driver, URL_COINMATICS.get('exchange_accounts'))
        page_exchange_accounts.open()
        page_exchange_accounts.Delete_api_key(API_BINANCE.get('api_name'))
        expected_results = ('Exchange Accounts - Coinmatics', 'Биржевые аккаунты - Coinmatics', 'Account di Exchange - Coinmatics')
        assert driver.title in expected_results


