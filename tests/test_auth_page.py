from ..pages.auth_page import AuthPage
import pytest
import os


def test_successful_authorization():
    page = AuthPage()
    page.tab_mail_click()
    page.enter_username(os.getenv('EMAIL_COR'))
    page.enter_password(os.getenv('PASSWORD_COR'))
    page.button_click()
    assert page.driver.current_url.startswith('https://b2c.passport.rt.ru/account_b2c/page')


@pytest.mark.parametrize('email, password',
                         [('latinic@mail.ru', 'OIUYTRbghvn54'),
                          (os.getenv('EMAIL_COR'), 'OIUYTRbghvn54')],
                         ids=['incorrect email', 'incorrect password'])
def test_unsuccessful_authorization(email, password):
    page = AuthPage()
    page.tab_mail_click()
    page.enter_username(email)
    page.enter_password(password)
    page.button_click()

    try:
        page.driver.find_element("id", "form-error-message")
    except Exception as NoSuchElementException:
        result = False
    else:
        result = True
    assert result


def test_unsuccessful_authorization_empty_phone():
    page = AuthPage()
    page.tab_phone_click()
    page.button_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Введите номер телефона')]")
    except Exception as NoSuchElementException:
        result = False
    else:
        result = True
    assert result


def test_unsuccessful_authorization_empty_mail():
    page = AuthPage()
    page.tab_mail_click()
    page.button_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Введите адрес, указанный при регистрации')]")
    except Exception as NoSuchElementException:
        result = False
    else:
        result = True
    assert result


def test_unsuccessful_authorization_empty_login():
    page = AuthPage()
    page.tab_login_click()
    page.button_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Введите логин, указанный при регистрации')]")
    except Exception as NoSuchElementException:
        result = False
    else:
        result = True
    assert result


def test_unsuccessful_authorization_empty_ls():
    page = AuthPage()
    page.tab_ls_click()
    page.button_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Введите номер вашего лицевого счета')]")
    except Exception as NoSuchElementException:
        result = False
    else:
        result = True
    assert result
