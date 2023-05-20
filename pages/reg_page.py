from .base_page import BasePage
from .locators import RegLocators


class RegPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_yvc6jRZvHc'
        driver.get(url)
        driver.find_element("id", "kc-register").click()

        self.name = driver.find_element(*RegLocators.REG_NAME)
        self.lastname = driver.find_element(*RegLocators.REG_LASTNAME)
        self.address = driver.find_element(*RegLocators.REG_ADDRESS)
        self.password = driver.find_element(*RegLocators.REG_PASSWORD)
        self.password_confirm = driver.find_element(*RegLocators.REG_PASSWORD_CONFIRM)
        self.button = driver.find_element(*RegLocators.REG_BUTTON)

    def enter_name(self, value):
        self.name.clear()
        self.name.send_keys(value)

    def enter_lastname(self, value):
        self.lastname.clear()
        self.lastname.send_keys(value)

    def enter_address(self, value):
        self.address.clear()
        self.address.send_keys(value)

    def enter_password(self, value):
        self.password.clear()
        self.password.send_keys(value)

    def enter_password_confirm(self, value):
        self.password_confirm.clear()
        self.password_confirm.send_keys(value)

    def name_click(self):
        self.name.click()

    def lastname_click(self):
        self.lastname.click()

    def button_click(self):
        self.button.click()

