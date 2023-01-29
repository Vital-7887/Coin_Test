import time
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator

class Delete_api_key(BasePage):
    locators = All_Locator

    def Delete_api_key_from_account_page(self, api_name):
        self.api_name = api_name
        exchange_account_item = (By.XPATH, "//div[text()= '" + self.api_name + "' ]")
        self.element_is_present(exchange_account_item).click()
        self.element_is_present(self.locators.modal_menu).click()
        self.element_is_visible(self.locators.second_item_modal_menu).click()
        self.element_is_visible(self.locators.button_delete_account_on_modal_window).click()
        added_exchange_accounts = (self.elements_are_present(self.locators.added_exchange_account_item))

        added_exchange_accounts_names = []

        for account in added_exchange_accounts:
            added_exchange_accounts_names.append(account.text)

        assert self.api_name not in added_exchange_accounts_names
        time.sleep(5)




