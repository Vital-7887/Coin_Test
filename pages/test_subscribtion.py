import time
import pytest
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator
from selenium.common.exceptions import TimeoutException
from consts import USER, API_BYBIT

class TestsSubscription(BasePage):
    locators = All_Locator

    def Subscribe_bybit_spot_strategy(self):
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        self.element_is_visible(self.locators.dropdown_bybit_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()
        self.element_is_clickable(self.locators.subscription_modal_window_2_step_button).click()
        # time.sleep(2)
        self.element_is_visible(self.locators.dropdown_alignment_method).click()
        self.element_is_visible(self.locators.manual_alignment_item).click()
        self.element_is_visible(self.locators.start_copying_button).click()
        time.sleep(5)
