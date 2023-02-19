import time
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator



class Subscription(BasePage):
    locators = All_Locator

    def Subscribe_to_spot_strategy(self, api_name):

        self.api_name = api_name
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        dropdown_item = (By.XPATH,  "//div[text()= '" + self.api_name + "' ]")
        self.element_is_visible(dropdown_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()
        # setting stop loss value
        # self.element_is_present(self.locators.stop_loss_field).click()
        # self.element_is_present(self.locators.enabled_stop_loss_item).click()
        # self.element_is_present(self.locators.value_stop_loss_field).send_keys(Keys.BACK_SPACE)
        # self.element_is_present(self.locators.value_stop_loss_field).send_keys(Keys.BACK_SPACE)
        # self.element_is_present(self.locators.value_stop_loss_field).click()
        # self.element_is_present(self.locators.value_stop_loss_field).send_keys(random.randint(5, 95))
        # time.sleep(3)
        # expected_result_stop_loss_value = self.element_is_present(self.locators.value_stop_loss_field).get_attribute('value')
        # # setting stop loss convert
        # self.element_is_present(self.locators.convert_stop_loss_field).click()
        # convert_to = [self.element_is_present(self.locators.convert_stop_loss_value_usdt), self.element_is_present(self.locators.convert_stop_loss_value_btc)]
        # convert_to[random.randint(0, 1)].click()
        # time.sleep(2)

        # setting blacklist

        # setting trader alignment
        self.element_is_present(self.locators.trader_alignment_dropdown).click()
        time.sleep(2)
        enable_trader_alignment = self.element_is_clickable(self.locators.trader_alignment_enabled_button)
        disabled_trader_alignment = self.element_is_clickable(self.locators.trader_alignment_disabled_button)
        trader_alignment_value = [enable_trader_alignment, disabled_trader_alignment]
        trader_alignment_value[random.randint(0, 1)].click()
        time.sleep(2)
        expected_result_trader_alignment = self.element_is_present(self.locators.trader_alignment_dropdown).text

        # expected_result_stop_loss_convert = self.element_is_visible(self.locators.convert_stop_loss_field).text
        self.element_is_clickable(self.locators.subscription_modal_window_2_step_button).click()
        self.element_is_visible(self.locators.dropdown_alignment_method).click()
        self.element_is_visible(self.locators.manual_alignment_item).click()
        self.element_is_visible(self.locators.start_copying_button).click()
        time.sleep(5)
        # actual_result_stop_loss_convert = self.element_is_present(self.locators.stop_loss_convert_to_value_on_subscription_page).text
        # actual_result_stop_loss_value = (self.element_is_present(self.locators.stop_loss_value_on_subscription_page).text).replace('%', "")
        # expected_result_stop_loss_value_int = int(expected_result_stop_loss_value)
        # actual_result_stop_loss_value_int = int(actual_result_stop_loss_value)
        actual_result_trader_alignment_value = self.element_is_present(self.locators.trader_alignment_value_on_subscription_page).text

        # assert expected_result_stop_loss_value_int == actual_result_stop_loss_value_int
        # assert expected_result_stop_loss_convert == actual_result_stop_loss_convert
        assert expected_result_trader_alignment == actual_result_trader_alignment_value



    def Subscribe_to_futures_strategy_with_autoalighn(self, api_name):
        self.api_name = api_name
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        dropdown_item = (By.XPATH,  "//div[text()= '" + self.api_name + "' ]")
        self.element_is_visible(dropdown_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()
        self.element_is_clickable(self.locators.subscription_modal_window_2_step_button).click()
        self.element_is_visible(self.locators.dropdown_alignment_method).click()
        self.element_is_visible(self.locators.manual_alignment_item).click()
        self.element_is_visible(self.locators.start_copying_button).click()


    def Subscribe_to_futures_srtategy_without_autoalighn(self, api_name):
        self.api_name = api_name
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        dropdown_item = (By.XPATH, "//div[text()= '" + self.api_name + "' ]")
        self.element_is_visible(dropdown_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()
        self.element_is_clickable(self.locators.start_copying_button).click()
        time.sleep(5)




