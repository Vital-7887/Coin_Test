import time

import allure
import pytest
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator
from selenium.common.exceptions import TimeoutException
from consts import USER, API_BYBIT, API_BINANCE


class LogInAndAddApi(BasePage):
    locators = All_Locator
    @allure.step("Login user")
    def Log_in_user(self):
        self.element_is_visible(self.locators.LOG_IN_button).click()
        with allure.step("filling fielders"):
            self.element_is_visible(self.locators.username_field).send_keys(USER.get('name'))
            self.element_is_visible(self.locators.password_field).send_keys(USER.get('password'))
        with allure.step("click submit button"):
            self.element_is_visible(self.locators.log_in_button).click()
    @allure.step("Add Bybit api key ")
    def Add_API_Key_Bybit(self):
        self.element_is_present(self.locators.add_account_button).click()
        self.element_is_visible(self.locators.select_exchange_button_Bybit).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.next_step_button).click()
        with allure.step(("api key data input")):
            self.element_is_visible(self.locators.name_api_key_field).send_keys(API_BYBIT.get('api_name'))
            self.element_is_visible(self.locators.api_key_field).send_keys(API_BYBIT.get('api_key'))
            self.element_is_visible(self.locators.secret_key_field).send_keys(API_BYBIT.get('secret_key'))
        with allure.step("Click submit button"):
            self.element_is_visible(self.locators.add_account_button_step3).click()
        try:
            self.element_is_visible(self.locators.done_button).click()
        except TimeoutException:
            pytest.fail(f"  Valid Bybit exchange API key  {API_BYBIT.get('api_name')}  NOT added  ")

    @allure.step("Add Binance api key ")
    def Add_API_Key_Binance(self):
        self.element_is_visible(self.locators.add_account_button).click()
        self.element_is_visible(self.locators.select_exchange_button_Binance).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.next_step_button).click()
        with allure.step(("api key data input")):
            self.element_is_visible(self.locators.name_api_key_field).send_keys(API_BINANCE.get('api_name'))
            self.element_is_visible(self.locators.api_key_field).send_keys(API_BINANCE.get('api_key'))
            self.element_is_visible(self.locators.secret_key_field).send_keys(API_BINANCE.get('secret_key'))
        with allure.step("Click submit button"):
            self.element_is_visible(self.locators.add_account_button_step3).click()
        try:
            self.element_is_visible(self.locators.done_button).click()
        except TimeoutException:
            pytest.fail(f"  Valid Binance exchange API key  {API_BINANCE.get('api_name')}  NOT added  ")

    @allure.step("Add OKX api key ")
    def Add_API_Key_OKX(self, api_name, api_key,secret_key,api_password):
        self.api_name = api_name
        self.api_key = api_key
        self.secret_key = secret_key
        self.api_password = api_password
        self.element_is_visible(self.locators.add_account_button).click()
        self.element_is_visible(self.locators.select_exchange_button_OKX).click()
        self.element_is_visible(self.locators.next_step_button).click()
        self.element_is_visible(self.locators.next_step_button).click()
        with allure.step(("api key data input")):
            self.element_is_visible(self.locators.name_api_key_field).send_keys(api_name)
            self.element_is_visible(self.locators.api_key_field).send_keys(api_key)
            self.element_is_visible(self.locators.secret_key_field).send_keys(secret_key)
            self.element_is_visible(self.locators.password_api_field).send_keys(api_password)
        with allure.step("Click submit button"):
            self.element_is_visible(self.locators.add_account_button_step3).click()
        try:
            self.element_is_visible(self.locators.done_button).click()
        except TimeoutException:
            pytest.fail(f"  Valid OKX exchange API key  {api_name}  NOT added  ")

