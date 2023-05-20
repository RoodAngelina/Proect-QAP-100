from selenium.webdriver.common.by import By

class RegLocators:
    REG_NAME = (By.NAME, "firstName")
    REG_LASTNAME = (By.NAME, "lastName")
    REG_ADDRESS = (By.ID, "address")
    REG_PASSWORD = (By.ID, "password")
    REG_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    REG_BUTTON = (By.NAME, "register")

class AuthLocators:
    AUTH_TAB_PHONE = (By.ID, "t-btn-tab-phone")
    AUTH_TAB_MAIL = (By.ID, "t-btn-tab-mail")
    AUTH_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_TAB_LS = (By.ID, "t-btn-tab-ls")
    AUTH_USERNAME = (By.ID, "username")
    AUTH_PASSWORD = (By.ID, "password")
    AUTH_BUTTON = (By.ID, "kc-login")
