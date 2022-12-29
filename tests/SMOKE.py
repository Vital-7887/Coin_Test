import time
from pages.test_elements_page import Tests


class Test_Smoke:

    def test_log_in(self, driver):
        test_page_main = Tests(driver, 'https://testing.coinmatics.com/')
        test_page_main.open()
        test_page_main.Log_in_user()
        time.sleep(5)
        expected_results = ('Dashboard - Coinmatics', 'Главная - Coinmatics', 'Cruscotto - Coinmatics')
        assert driver.title in expected_results

    def test_add_api_bybit(self, driver):
        valid_api_bybit = Tests(driver, 'https://testing.coinmatics.com/app/accounts/exchange-accounts/')
        valid_api_bybit.open()
        valid_api_bybit.Add_API_Key_Bybit()
        time.sleep(3)

    def test_add_api_binance(self, driver):
        valid_api_binance = Tests(driver, 'https://testing.coinmatics.com/ru/app/accounts/exchange-accounts/')
        valid_api_binance.open()
        valid_api_binance.Add_API_Key_Binance()
        time.sleep(3)

    def test_add_api_okx(self, driver):
        valid_api_okx = Tests(driver, 'https://testing.coinmatics.com/ru/app/accounts/exchange-accounts/')
        valid_api_okx.open()
        valid_api_okx.Add_API_Key_OKX()
        time.sleep(3)
