import time
import pytest
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator
from selenium.common.exceptions import TimeoutException
from consts import USER, API_BYBIT, API_BINANCE, API_OKX


class LogInAndAddApi(BasePage):
    locators = All_Locator

    def Log_in_user(self):
        self.element_is_visible(self.locators.LOG_IN_button).click()
        self.element_is_visible(self.locators.username_field).send_keys(USER.get('name'))
        self.element_is_visible(self.locators.password_field).send_keys(USER.get('password'))
        self.element_is_visible(self.locators.log_in_button).click()

    def Add_API_Key_Bybit(self):
        self.element_is_visible(self.locators.add_account_button).click()
        self.element_is_visible(self.locators.select_exchange_button_Bybit).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.name_api_key_field).send_keys(API_BYBIT.get('api_name'))
        self.element_is_visible(self.locators.api_key_field).send_keys(API_BYBIT.get('api_key'))
        self.element_is_visible(self.locators.secret_key_field).send_keys(API_BYBIT.get('secret_key'))
        time.sleep(2)
        self.element_is_visible(self.locators.add_account_button_step3).click()
        try:
            self.element_is_visible(self.locators.done_button).click()
        except TimeoutException:
            pytest.fail(f"  Valid Bybit exchange API key  {API_BYBIT.get('api_name')}  NOT added  ")



    def Add_API_Key_Binance(self):
        self.element_is_visible(self.locators.add_account_button).click()
        self.element_is_visible(self.locators.select_exchange_button_Binance).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.name_api_key_field).send_keys(API_BINANCE.get('api_name'))
        self.element_is_visible(self.locators.api_key_field).send_keys(API_BINANCE.get('api_key'))
        self.element_is_visible(self.locators.secret_key_field).send_keys(API_BINANCE.get('secret_key'))
        time.sleep(2)
        self.element_is_visible(self.locators.add_account_button_step3).click()
        try:
            self.element_is_visible(self.locators.done_button).click()
        except TimeoutException:
            pytest.fail(f"  Valid Binance exchange API key  {API_BINANCE.get('api_name')}  NOT added  ")


    def Add_API_Key_OKX(self):
        self.element_is_visible(self.locators.add_account_button).click()
        self.element_is_visible(self.locators.select_exchange_button_OKX).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.name_api_key_field).send_keys(API_OKX.get('api_name'))
        self.element_is_visible(self.locators.api_key_field).send_keys(API_OKX.get('api_key'))
        self.element_is_visible(self.locators.secret_key_field).send_keys(API_OKX.get('secret_key'))
        self.element_is_visible(self.locators.password_api_field).send_keys(API_OKX.get('api_password'))
        time.sleep(2)
        self.element_is_visible(self.locators.add_account_button_step3).click()
        try:
            self.element_is_visible(self.locators.done_button).click()
        except TimeoutException:
            pytest.fail(f"  Valid OKX exchange API key  {API_OKX.get('api_name')}  NOT added  ")

