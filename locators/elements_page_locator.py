from selenium.webdriver.common.by import By
from consts import API_BYBIT


class All_Locator:
    # Landing page
    LOG_IN_button = (By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/div[2]/a[1]')

    # Log In page
    username_field = (By.XPATH, '//*[@id="1"]')
    password_field = (By.XPATH, '//*[@id="2"]')
    log_in_button = (By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/form/div[3]/button')

    # sidebar
    sidebar_accounts_link = (By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div[4]/button/div[1]/div')
    sidebar_exchange_accounts_link = (By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div[4]/div/div[1]/a/div[2]')

    # Exchange account page
    add_account_button = (By.XPATH,'//button[@class = "styles__StyledButton-sc-1afd7sh-0 TiwWY styles__AddAccountButton-sc-1bkxcrr-10 eSCXrN"]')

    # add new exchange account modal window
    select_exchange_button_Bybit = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[3]/button')
    select_exchange_button_Binance = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/button')
    select_exchange_button_OKX = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/button')
    next_step_button = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/button[2]')
    name_api_key_field = (By.XPATH, '//*[@id="1"]')
    api_key_field = (By.XPATH, '//*[@id="2"]')
    secret_key_field = (By.XPATH, '//*[@id="3"]')
    password_api_field = (By.XPATH, '//*[@id="4"]')
    add_account_button_step3 = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/button[2]')
    done_button = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/button')

    # strategy page
    subscribe_to_copytrading_button = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[2]/div[2]/div[1]/button')

    # copytrading subscription modal window
    dropdown_select_account = (By.XPATH, '//div[@class="styles__H4-sc-1ri3tpl-3 styles__DropdownDefaultBlockTitle-sc-8l8a2d-3 cKbycB gEDzBX"]')
    subscription_modal_window_1_step_button = (By.XPATH, '//button[@class = "styles__StyledButton-sc-1afd7sh-0 iYbZDF styles__ApplyButton-sc-1piieu7-18 fnyORG"]')
    subscription_modal_window_2_step_button = (By.XPATH, '//button[@class = "styles__StyledButton-sc-1afd7sh-0 iYbZDF"]')
    dropdown_alignment_method = (By.XPATH, '//div[@class = "styles__DropdownBlock-sc-10gtvvv-1 styles__DropdownItem-sc-10gtvvv-6 leMWGX hDCSwg"]')
    manual_alignment_item = (By.XPATH, '//div[@class ="styles__DropdownBlock-sc-10gtvvv-1 styles__DropdownItem-sc-10gtvvv-6 leMWGX bXxglf"]')
    start_copying_button = (By.XPATH, '//button[@class ="styles__StyledButton-sc-1afd7sh-0 jSiKd"]')

    # stop loss
    stop_loss_field = (By.XPATH, '//button[@class ="styles__DropdownToggler-sc-s7kz7k-4 bzJcXx"][1]')
    enabled_stop_loss_item = (By.XPATH, '//button[@class = "styles__Option-sc-s7kz7k-7 ibhdvx"]')
    value_stop_loss_field = (By.XPATH, '//input[@class="styles__StyledInput-sc-1ioa5fk-3 deOWdE"]')

    # convert_stop_loss_field = (By.XPATH, '//div[@class = "styles__Text-sc-s7kz7k-9 hxQiqI"][text() = "USDT"]')
    convert_stop_loss_field = (By.XPATH, '//div[@class = "styles__StopLossFields-sc-1gyq91b-8 forSpP"]/div[@class = "styles__Wrapper-sc-s7kz7k-0 kpNwKf styles__Select-sc-1gyq91b-7 dcMkLV"]//div[@class = "styles__Text-sc-s7kz7k-9 hxQiqI"]')
    convert_stop_loss_value_usdt = (By.XPATH, '//button[@class = "styles__Option-sc-s7kz7k-7 ibhdvx"]')
    convert_stop_loss_value_btc = (By.XPATH, '//button[@class = "styles__Option-sc-s7kz7k-7 bnYHls"]')

    # coin black list
    add_coin_button = (By.XPATH, '//span[@class = "styles__Icon-sc-1afd7sh-1 bDqrp"]')
    type_coin_name_input = (By.NAME, "coin")
    blacklisted_coin = (By.XPATH, '//div[@class ="styles__BlackListText-sc-1gyq91b-13 fpRXex"]')

    # auto alignment
    trader_alignment_dropdown = (By.ID, '3')
    trader_alignment_enabled_button = (By.XPATH, '//button[@class = "styles__Option-sc-s7kz7k-7 ibhdvx"]')
    trader_alignment_disabled_button = (By.XPATH, '//button[@class = "styles__Option-sc-s7kz7k-7 bnYHls"]')
    scheduled_alignment_dropdown = (By.ID, '4')
    scheduled_alignment_enabled_button = (By.XPATH, '//button[@class = "styles__Option-sc-s7kz7k-7 ibhdvx"]')
    scheduled_alignment_frequency_dropdown = (By.XPATH, '//div[@id="5"]//div[@class = "styles__Text-sc-s7kz7k-9 hxQiqI"]')

    # my accounts block on exchange accounts' page
    modal_menu = (By.XPATH, '//div[@class="styles__OptionsButton-sc-1rikj74-1 hfdLhs"]')
    added_exchange_account_item = (By.XPATH, '//div[@class = "styles__ItemTitle-sc-8hcuzp-2 bTsnVE"]')
    added_exchange_account_value = (By.XPATH, '//div[@class = "styles__Item-sc-8hcuzp-1 jlyGJE"][contains(text(),"USDT")]')
    dropdown_number_of_exchange_accounts_on_the_page = (By.XPATH, '//div[@class = "styles__TextPlaceholder-sc-s7kz7k-11 hrMjTn"][1]')
    button_all_exchange_accounts_on_the_page = (By.XPATH, '//button[@class = "styles__Option-sc-s7kz7k-7 ibhdvx"][3]')

    # delete account modal manu on account's page
    second_item_modal_menu = (By.XPATH, '//button[@class="styles__DropdownItem-sc-1opd8lr-3 jRkwJS"][2] ')

    # delete account modal window
    button_delete_account_on_modal_window = (By.XPATH, '//button[@class="styles__StyledButton-sc-1afd7sh-0 jSiKd"] ')

    # subscription_page
    stop_loss_value_on_subscription_page = (By.ID, 'stop-loss-value')
    stop_loss_convert_to_value_on_subscription_page = (By.ID, 'stop-loss-currency')
    trader_alignment_value_on_subscription_page = (By.ID, 'trader-alignment-ability')
    coin_black_list_on_subscription_page = (By.XPATH, '//div[@class = "styles__BlackListText-sc-l28p96-11 jGtyMa"]')
    scheduled_alignment_value_on_subscription_page = (By.ID, 'auto-alignment-schedule')









