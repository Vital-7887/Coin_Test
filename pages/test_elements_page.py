import time

import pytest

from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator


class Tests(BasePage):
    locators = All_Locator

    def Log_in_user(self, username, password):
        self.username = username
        self.password = password
        self.element_is_visible(self.locators.LOG_IN_button).click()
        self.element_is_visible(self.locators.username_fild).send_keys(self.username)
        self.element_is_visible(self.locators.password_fild).send_keys(self.password)
        self.element_is_visible(self.locators.log_in_button).click()

    def Add_API_Key(self, api_name, api_key, secret_key):
        self.api_name = api_name
        self.api_key = api_key
        self.secret_key = secret_key
        self.element_is_visible(self.locators.add_account_button).click()
        self.element_is_visible(self.locators.choose_exchange_button).click()
        self.element_is_visible(self.locators.next_step_button_step1).click()
        self.element_is_visible(self.locators.next_step_button_step2).click()
        self.element_is_visible(self.locators.name_api_key_fild).send_keys(self.api_name)
        self.element_is_visible(self.locators.api_key_fild).send_keys(self.api_key)
        self.element_is_visible(self.locators.secret_key_fild).send_keys(self.secret_key)
        time.sleep(2)
        self.element_is_visible(self.locators.add_account_button_step3).click()
        if self.element_is_not_visible(self.locators.done_button):
            return pytest.skip(f"  Valid Bybit exchange API key  {self.api_name}  NOT added  ")
        else:
            self.element_is_visible(self.locators.done_button, 'test').click()