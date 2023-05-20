from ..pages.reg_page import RegPage
from elements import driver
import os

name_ = 'Ян'
lastname_ = 'Янский'
email_ = os.getenv('EMAIL')
password_ = 'Asdfghj#'
phone_ = '+375999999999'

def test_successful_first_step_registration_email():
    page = RegPage()
    page.enter_name(name_)
    page.enter_lastname(lastname_)
    page.enter_address(email_)
    page.enter_password(password_)
    page.enter_password_confirm(password_)
    page.button_click()

    assert page.driver.current_url.startswith(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution')


def test_successful_first_step_registration_phone():
    page = RegPage()
    page.enter_name(name_)
    page.enter_lastname(lastname_)
    page.enter_address(phone_)
    page.enter_password(password_)
    page.enter_password_confirm(password_)
    page.button_click()

    assert page.driver.current_url.startswith(
        'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution')


def test_registration_empty_fields():
    page = RegPage()
    page.button_click()
    try:
        driver.find_elements("xpath",
                             "//span[contains(text(), 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.')]")
        driver.find_elements("xpath",
                             "//span[contains(text(), 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.')]")
        driver.find_elements("xpath",
                             "//span[contains(text(), 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru')]")
        driver.find_elements("xpath",
                             "//span[contains(text(), 'Длина пароля должна быть не менее 8 символов')]")
        driver.find_elements("xpath",
                             "//span[contains(text(), 'Длина пароля должна быть не менее 8 символов')]")
    except Exception as NoSuchElementException:
        result = False
    else:
        result = True
    assert result
