import time
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from locators.elements_page_locator import All_Locator


class Subscription(BasePage):
    locators = All_Locator

    def Subscribe_to_strategy_with_autoalign(self, api_name):
        self.api_name = api_name
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        dropdown_item = (By.XPATH,  "//div[text()= '" + self.api_name + "' ]")
        self.element_is_visible(dropdown_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()
        self.element_is_clickable(self.locators.subscription_modal_window_2_step_button).click()
        # time.sleep(2)
        self.element_is_visible(self.locators.dropdown_alignment_method).click()
        self.element_is_visible(self.locators.manual_alignment_item).click()
        self.element_is_visible(self.locators.start_copying_button).click()
        time.sleep(5)


    def Subscribe_to_srtategy_without_autoalighn(self, api_name):
        self.api_name=api_name
        self.element_is_visible(self.locators.subscribe_to_copytrading_button).click()
        self.element_is_visible(self.locators.dropdown_select_account).click()
        dropdown_item = (By.XPATH, "//div[text()= '" + self.api_name + "' ]")
        self.element_is_visible(dropdown_item).click()
        self.element_is_clickable(self.locators.subscription_modal_window_1_step_button).click()
        self.element_is_clickable(self.locators.start_copying_button).click()
        time.sleep(5)




