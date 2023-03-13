import time
import random
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator
from consts import COIN_LIST

class Subscription(BasePage):
    locators = All_Locator

    def Setting_stop_loss_value(self):
        self.element_is_present(self.locators.stop_loss_field).click()
        self.element_is_present(self.locators.enabled_stop_loss_item).click()
        self.element_is_present(self.locators.value_stop_loss_field).send_keys(Keys.BACK_SPACE)
        self.element_is_present(self.locators.value_stop_loss_field).send_keys(Keys.BACK_SPACE)
        self.element_is_present(self.locators.value_stop_loss_field).click()
        self.element_is_present(self.locators.value_stop_loss_field).send_keys(random.randint(5, 95))
        time.sleep(1)
        return int(self.element_is_present(self.locators.value_stop_loss_field).get_attribute('value'))

    def Settinng_stop_loss_convert(self):
        self.element_is_present(self.locators.convert_stop_loss_field).click()
        convert_to = [self.element_is_present(self.locators.convert_stop_loss_value_usdt),
                      self.element_is_present(self.locators.convert_stop_loss_value_btc)]
        convert_to[random.randint(0, 1)].click()
        time.sleep(1)
        return self.element_is_visible(self.locators.convert_stop_loss_field).text

    def Setting_black_list_coin(self):
        self.element_is_present(self.locators.add_coin_button).click()
        time.sleep(1)
        self.element_is_present(self.locators.type_coin_name_input).click()
        time.sleep(1)
        coin = COIN_LIST[random.randint(0, 44)]
        self.element_is_present(self.locators.type_coin_name_input).send_keys(coin)
        self.element_is_present(self.locators.type_coin_name_input).send_keys(Keys.RETURN)
        return self.element_is_present(self.locators.blacklisted_coin).text

    def Setting_trader_alignment(self):
        self.element_is_present(self.locators.trader_alignment_dropdown).click()
        time.sleep(1)
        enable_trader_alignment = self.element_is_clickable(self.locators.trader_alignment_enabled_button)
        disabled_trader_alignment = self.element_is_clickable(self.locators.trader_alignment_disabled_button)
        trader_alignment_value = [enable_trader_alignment, disabled_trader_alignment]
        trader_alignment_value[random.randint(0, 1)].click()
        time.sleep(1)
        return self.element_is_present(self.locators.trader_alignment_dropdown).text

    def Setting_scheduled_alignment(self):
        self.element_is_present(self.locators.scheduled_alignment_dropdown).click()
        self.element_is_present(self.locators.scheduled_alignment_enabled_button).click()
        self.element_is_present(self.locators.scheduled_alignment_frequency_dropdown).click()
        number_item = str(random.randint(1, 9))
        scheduled_alignment_frequency_dropdown_item = (
            By.XPATH, "//button[@class='styles__Option-sc-s7kz7k-7 ibhdvx'][" + number_item + "]")
        self.element_is_present(scheduled_alignment_frequency_dropdown_item).click()
        time.sleep(1)
        return self.element_is_present(self.locators.scheduled_alignment_frequency_dropdown).text

    def Subscribe_to_spot_strategy(self, api_name):

        self.api_name = api_name
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        dropdown_item = (By.XPATH,  "//div[text()= '" + self.api_name + "' ]")
        self.element_is_visible(dropdown_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()

        expected_result_stop_loss_value = self.Setting_stop_loss_value()
        expected_result_stop_loss_convert = self.Settinng_stop_loss_convert()
        expected_result_coin_black_list = self.Setting_black_list_coin()
        expected_result_trader_alignment = self.Setting_trader_alignment()
        expected_result_scheduled_alignment_frequency = self.Setting_scheduled_alignment()

        self.element_is_clickable(self.locators.subscription_modal_window_2_step_button).click()
        self.element_is_visible(self.locators.dropdown_alignment_method).click()
        self.element_is_visible(self.locators.manual_alignment_item).click()
        self.element_is_visible(self.locators.start_copying_button).click()
        time.sleep(5)

        actual_result_stop_loss_convert = self.element_is_present(
            self.locators.stop_loss_convert_to_value_on_subscription_page).text
        actual_result_stop_loss_value = int(
            (self.element_is_present(self.locators.stop_loss_value_on_subscription_page).text).replace('%', ""))
        actual_result_coin_black_list = self.element_is_present(
            self.locators.coin_black_list_on_subscription_page).text
        actual_result_trader_alignment_value = self.element_is_present(
            self.locators.trader_alignment_value_on_subscription_page).text
        actual_result_scheduled_alignment_frequency = self.element_is_present(
            self.locators.scheduled_alignment_value_on_subscription_page).text

        assert expected_result_stop_loss_value == actual_result_stop_loss_value
        assert expected_result_stop_loss_convert == actual_result_stop_loss_convert
        assert expected_result_trader_alignment == actual_result_trader_alignment_value
        assert expected_result_scheduled_alignment_frequency == actual_result_scheduled_alignment_frequency
        assert expected_result_coin_black_list == actual_result_coin_black_list



    def Subscribe_to_futures_strategy_with_autoalign(self, api_name):
        self.api_name = api_name
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        dropdown_item = (By.XPATH,  "//div[text()= '" + self.api_name + "' ]")
        self.element_is_visible(dropdown_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()

        expected_result_coin_black_list = self.Setting_black_list_coin()
        expected_result_trader_alignment = self.Setting_trader_alignment()
        expected_result_scheduled_alignment_frequency = self.Setting_scheduled_alignment()

        self.element_is_clickable(self.locators.subscription_modal_window_2_step_button).click()
        self.element_is_visible(self.locators.dropdown_alignment_method).click()
        self.element_is_visible(self.locators.manual_alignment_item).click()
        self.element_is_visible(self.locators.start_copying_button).click()
        time.sleep(5)

        actual_result_coin_black_list = self.element_is_present(self.locators.coin_black_list_on_subscription_page).text
        actual_result_trader_alignment_value = self.element_is_present(
            self.locators.trader_alignment_value_on_subscription_page).text
        actual_result_scheduled_alignment_frequency = self.element_is_present(
            self.locators.scheduled_alignment_value_on_subscription_page).text

        assert expected_result_trader_alignment == actual_result_trader_alignment_value
        assert expected_result_scheduled_alignment_frequency == actual_result_scheduled_alignment_frequency
        assert expected_result_coin_black_list == actual_result_coin_black_list


    def Subscribe_to_futures_srtategy_without_autoalighn(self, api_name):
        self.api_name = api_name
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        dropdown_item = (By.XPATH, "//div[text()= '" + self.api_name + "' ]")
        self.element_is_visible(dropdown_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()

        expected_result_coin_black_list = self.Setting_black_list_coin()

        self.element_is_clickable(self.locators.start_copying_button).click()
        time.sleep(5)

        actual_result_coin_black_list = self.element_is_present(self.locators.coin_black_list_on_subscription_page).text

        assert expected_result_coin_black_list == actual_result_coin_black_list





