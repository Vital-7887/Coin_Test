import time
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator


class Balance_api_key_is_not_zero(BasePage):
    locators = All_Locator

    def Balance_is_not_zero(self):

        self.element_is_visible(self.locators.dropdown_number_of_exchange_accounts_on_the_page).click()
        self.element_is_visible(self.locators.button_all_exchange_accounts_on_the_page).click()

        added_accounts = self.elements_are_present(self.locators.added_exchange_account_value)
        added_accounts_value = []

        time.sleep(3)
        for value in added_accounts:
            added_accounts_value.append(value.text)

        assert '0.0000 USDT' not in added_accounts_value
