from .base_page import BasePage
from .locators import AuthLocators


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_yvc6jRZvHc'
        driver.get(url)

        self.tab_phone = driver.find_element(*AuthLocators.AUTH_TAB_PHONE)
        self.tab_mail = driver.find_element(*AuthLocators.AUTH_TAB_MAIL)
        self.tab_login = driver.find_element(*AuthLocators.AUTH_TAB_LOGIN)
        self.tab_ls = driver.find_element(*AuthLocators.AUTH_TAB_LS)
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_PASSWORD)
        self.button = driver.find_element(*AuthLocators.AUTH_BUTTON)

    def enter_username(self, value):
        self.username.clear()
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.clear()
        self.password.send_keys(value)

    def tab_phone_click(self):
        self.tab_phone.click()

    def tab_mail_click(self):
        self.tab_mail.click()

    def tab_login_click(self):
        self.tab_login.click()

    def tab_ls_click(self):
        self.tab_ls.click()

    def button_click(self):
        self.button.click()
