from selenium.webdriver.common.by import By
from consts import API_BYBIT


class All_Locator:
    # Landing page

    LOG_IN_button = (By.XPATH, '//*[@id="__next"]/div/header/div/div[1]/div[2]/a[1]')
    # Log In page

    username_fild = (By.XPATH, '//*[@id="1"]')
    password_fild = (By.XPATH, '//*[@id="2"]')
    log_in_button = (By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/form/div[3]/button')

    # sidebar
    sidebar_accaunts_link = (By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div[4]/button/div[1]/div')
    sidebar_exchange_accaunts_link = (By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div[4]/div/div[1]/a/div[2]')

    # Exchange account page
    add_account_button = (By.XPATH,'//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/button')

    # add new exchange account modal window
    choose_exchange_button_Bybit = (By.XPATH,'//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[3]/button')
    choose_exchange_button_Binance = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/button')
    choose_exchange_button_OKX = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/button')
    next_step_button_step1 = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/button[2]')
    next_step_button_step2 = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/button[2]')
    name_api_key_fild = (By.XPATH, '//*[@id="1"]')
    api_key_fild = (By.XPATH, '//*[@id="2"]')
    secret_key_fild = (By.XPATH, '//*[@id="3"]')
    password_api_fild = (By.XPATH, '//*[@id="4"]')
    add_account_button_step3 = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/button[2]')
    done_button = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/button')

    # strategy page
    subscribe_to_copytrading_button = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[2]/div[2]/div[1]/button')

    # copytrading subscription modal window

    dropdown_select_account = (By.XPATH, '//*[@id="__next"]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[3]/div/div/div/div[5]/div/div/div')
    subscription_modal_window_1_step_button = (By.XPATH, '//button[@class = "styles__StyledButton-sc-1afd7sh-0 iYbZDF styles__ApplyButton-sc-1piieu7-18 fnyORG"]')
    subscription_modal_window_2_step_button = (By.XPATH, '//button[@class = "styles__StyledButton-sc-1afd7sh-0 iYbZDF"]')
    dropdown_alignment_method = (By.XPATH, '//div[@class = "styles__DropdownBlock-sc-10gtvvv-1 styles__DropdownItem-sc-10gtvvv-6 leMWGX hDCSwg"]')
    manual_alignment_item = (By.XPATH, '//div[@class ="styles__DropdownBlock-sc-10gtvvv-1 styles__DropdownItem-sc-10gtvvv-6 leMWGX bXxglf"]')
    start_copying_button = (By.XPATH, '//button[@class ="styles__StyledButton-sc-1afd7sh-0 jSiKd"]')


    madal_menu = (By.XPATH, '//div[@class="styles__OptionsButton-sc-1rikj74-1 hfdLhs"]')
    second_item_modal_menu = (By.XPATH, '//button[@class="styles__DropdownItem-sc-1opd8lr-3 jRkwJS"][2] ')
    button_delete_account_on_modal_window = (By.XPATH, '//button[@class="styles__StyledButton-sc-1afd7sh-0 jSiKd"] ')
    added_exchange_account_item = (By.XPATH,'//div[@class = "styles__ItemTitle-sc-8hcuzp-2 bTsnVE"]')







