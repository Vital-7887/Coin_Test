from selenium.webdriver.common.by import By


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






