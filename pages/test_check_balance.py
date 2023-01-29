import time
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator


class Balance_api_key_is_not_zero(BasePage):
    locators = All_Locator

    def Balance_is_not_zero(self):

        added_accounts = self.elements_are_present(self.locators.added_exchange_account_value)
        added_accounts_value = []

        for value in added_accounts:
            added_accounts_value.append(value.text)

        assert '0.0000 USDT' not in added_accounts_value
