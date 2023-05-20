from ..pages.reg_page import RegPage
import pytest


def cyrill(n):
    return 'щ' * n

def latin(n):
    return 'w' * n

def spec_symb(n):
    return '%' * n

def digits(n):
    return '0' * n


@pytest.mark.parametrize('input_',
                         [(cyrill(2)), (cyrill(10)), (cyrill(30)), ('   ' + cyrill(10) + '   '),
                          (cyrill(4) + '-' + cyrill(4))],
                         ids=['2 cyrillic letters', '10 cyrillic letters', '30 cyrillic letters',
                              'gaps + 10 cyrillic letters + gaps', '8 cyrillic letters with a hyphen in the middle'])
def test_name_field_right(input_):
    page = RegPage()
    page.enter_name(input_)
    page.lastname_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'От 2 до 30 символов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert result


@pytest.mark.parametrize('input_',
                         [(cyrill(1)), (cyrill(31)), (cyrill(256)), (cyrill(4) + ' ' + cyrill(4)), (latin(10)),
                          (spec_symb(10)), (digits(10))],
                         ids=['1 cyrillic letter', '31 cyrillic letters', '256 cyrillic letters',
                              '8 cyrillic letters with a gap in the middle', 'latin letters (10)',
                              'spec.symbols (10)', 'digits (10)'])
def test_name_field_wrong(input_):
    page = RegPage()
    page.enter_name(input_)
    page.lastname_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'От 2 до 30 символов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_', [(cyrill(2)), (cyrill(10)), (cyrill(30)), ('   ' + cyrill(10) + '   '),
                                    (cyrill(4) + '-' + cyrill(4))],
                         ids=['2 cyrillic letters', '10 cyrillic letters', '30 cyrillic letters',
                              'gaps + 10 cyrillic letters + gaps', '8 cyrillic letters with a hyphen in the middle'])
def test_lastname_field_right(input_):
    page = RegPage()
    page.enter_lastname(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'От 2 до 30 символов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert result


@pytest.mark.parametrize('input_',
                         [(cyrill(1)), (cyrill(31)), (cyrill(256)), (cyrill(4) + ' ' + cyrill(4)), (latin(10)),
                          (spec_symb(10)), (digits(10))],
                         ids=['1 cyrillic letter', '31 cyrillic letters', '256 cyrillic letters',
                              '8 cyrillic letters with a gap in the middle', 'latin letters (10)',
                              'spec.symbols (10)', 'digits (10)'])
def test_lastname_field_wrong(input_):
    page = RegPage()
    page.enter_lastname(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'От 2 до 30 символов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


# pytest -v test_1.py::test_lastname_field_right test_1.py::test_lastname_field_wrong


@pytest.mark.parametrize('input_',
                         [('example@email.ru'), ('+375' + digits(9)), ('+7' + digits(10)), ('375' + digits(9)),
                          ('7' + digits(10)), ('  +37511-1  11-1111  '), ('   + 711  1-111-1111  ')],
                         ids=['example@email.ru', '+375XXXXXXXXX', '+7XXXXXXXXXX',
                              '375XXXXXXXXX', '7XXXXXXXXXX', '+375XXXXXXXXX with gaps and hyphens',
                              '+7XXXXXXXXXX with gaps'])
def test_address_field_right(input_):
    page = RegPage()
    page.enter_address(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Введите телефон в формате')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert result


@pytest.mark.parametrize('input_',
                         [(latin(7)), (cyrill(5) + '@mail.ru'), (spec_symb(6) + 'mail.ru'), ('.example@mail.ru'),
                          ('exa..mple@mail.ru'), ('example.@mail.ru'), ('+375' + digits(10)), ('+7' + digits(11)),
                          ('+375' + digits(8)), ('+7' + digits(9)), ('+375' + digits(19)), ('+7' + digits(20)),
                          (digits(15))],
                         ids=['latin letters', 'cyrillic@mail.ru', 'spec.symbols(not"-_.")@mail.ru',
                              '.example@mail.ru', 'exa..mple@mail.ru', 'example.@mail.ru', '+375XXXXXXXXX X',
                              '+7XXXXXXXXXX X', '+375XXXXXXXX (-1 digit)', '+7XXXXXXXXX (-1 digit)',
                              '+375XXXXXXXX +10 digits', '+7XXXXXXXXX +10 digits', '15 digits'])
def test_address_field_wrong(input_):
    page = RegPage()
    page.enter_address(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Введите телефон в формате')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(4) + latin(1).upper() + digits(2) + spec_symb(1)),
                          (latin(5) + latin(5).upper() + digits(10)),
                          ('   ' + latin(1) + latin(7).upper() + spec_symb(6) + '  ')],
                         ids=['5 latin letters (1 upper) + 2 digits + 1 spec.symbol',
                              '10 latin letters (5 upper) + 10 digits ',
                              'gaps + 8 latin letters (7 upper) + spec.symbols(6) + gaps'])
def test_password_field_right(input_):
    page = RegPage()
    page.enter_password(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath",
                            "//span[contains(text(), 'Пароль должен') or contains(text(), 'Пароль не должен') or contains(text(), 'Длина пароля')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert result


@pytest.mark.parametrize('input_',
                         [(latin(3) + latin(4).upper() + ' ' + digits(6))],
                         ids=['password with gaps in the middle'])
def test_password_field_wrong_gaps(input_):
    page = RegPage()
    page.enter_password(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Пароль не должен содержать пробелов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(7)), (cyrill(6)), (spec_symb(4)), (digits(1)),
                          (latin(4) + latin(1).upper() + spec_symb(1) + digits(1))],
                         ids=['7 latin letters', '6 cyrillic letters', '4 spec.symbols', '1 digit',
                              '5 latin letters (1 upper) + 1 spec.symbol + 1 digit'])
def test_password_field_wrong_short(input_):
    page = RegPage()
    page.enter_password(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Длина пароля должна быть не менее 8 символов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(21)), (cyrill(22)), (spec_symb(255)), (digits(256)),
                          (latin(300) + latin(100).upper() + spec_symb(300) + digits(300))],
                         ids=['21 latin letters', '22 cyrillic letters', '255 spec.symbols', '256 digits',
                              '400 latin letters (100 upper) + 300 spec.symbols + 300 digits'])
def test_password_field_wrong_long(input_):
    page = RegPage()
    page.enter_password(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Длина пароля должна быть не более 20 символов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(cyrill(8)), (cyrill(5) + latin(4)), (cyrill(12) + digits(7)),
                          (cyrill(15) + spec_symb(5)), (cyrill(8) + digits(2) + spec_symb(3))],
                         ids=['8 cyrillic letters', '5 cyrillic letters + 4 latin letters',
                              '12 cyrillic letters + 7 digits', '15 cyrillic letters + 5 spec.symbols',
                              '8 cyrillic letters + 2 digits + 3 spec.symbols '])
def test_password_field_wrong_cyrill(input_):
    page = RegPage()
    page.enter_password(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Пароль должен содержать только латинские буквы')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(8)), (latin(9).upper()), (latin(15) + latin(1).upper()),
                          (latin(1) + latin(19).upper())],
                         ids=['8 latin letters', '9 latin upper letters',
                              '16 latin letters (1 upper)', '20 latin letters (19 upper)'])
def test_password_field_wrong_without_dig_specsymb(input_):
    page = RegPage()
    page.enter_password(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath",
                            "//span[contains(text(), 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(7) + digits(1)), (latin(19) + spec_symb(1)), (latin(14) + digits(2) + spec_symb(3)),
                          (digits(12)), (spec_symb(9)), (digits(8) + spec_symb(6))],
                         ids=['7 latin letters + 1 digit', '19 latin letters + 1 spec.symbol',
                              '14 latin letters + 2 digits + 3 spec.symbols', '12 digits', '9 spec.symbols',
                              '8 digits + 6 spec.symbols'])
def test_password_field_wrong_without_upper(input_):
    page = RegPage()
    page.enter_password(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath",
                            "//span[contains(text(), 'Пароль должен содержать хотя бы одну заглавную букву')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(4).upper() + digits(2) + spec_symb(2)), (latin(7).upper() + digits(7)),
                          (latin(2).upper() + spec_symb(18))],
                         ids=['4 latin upper letters + 2 digit + 2 spec.symbols', '7 latin upper letters + 7 digits',
                              '2 latin upper letters + 18 spec.symbols'])
def test_password_field_wrong_without_lower(input_):
    page = RegPage()
    page.enter_password(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath",
                            "//span[contains(text(), 'Пароль должен содержать хотя бы одну строчную букву')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(4) + latin(1).upper() + digits(2) + spec_symb(1)),
                          (latin(5) + latin(5).upper() + digits(10)),
                          ('   ' + latin(1) + latin(7).upper() + spec_symb(6) + '  ')],
                         ids=['5 latin letters (1 upper) + 2 digits + 1 spec.symbol',
                              '10 latin letters (5 upper) + 10 digits ',
                              'gaps + 8 latin letters (7 upper) + spec.symbols(6) + gaps'])
def test_password_confirm_field_right(input_):
    page = RegPage()
    page.enter_password_confirm(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath",
                            "//span[contains(text(), 'Пароль должен') or contains(text(), 'Пароль не должен') or contains(text(), 'Длина пароля')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert result


@pytest.mark.parametrize('input_',
                         [(latin(3) + latin(4).upper() + ' ' + digits(6))],
                         ids=['password with gaps in the middle'])
def test_password_confirm_field_wrong_gaps(input_):
    page = RegPage()
    page.enter_password_confirm(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Пароль не должен содержать пробелов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(7)), (cyrill(6)), (spec_symb(4)), (digits(1)),
                          (latin(4) + latin(1).upper() + spec_symb(1) + digits(1))],
                         ids=['7 latin letters', '6 cyrillic letters', '4 spec.symbols', '1 digit',
                              '5 latin letters (1 upper) + 1 spec.symbol + 1 digit'])
def test_password_confirm_field_wrong_short(input_):
    page = RegPage()
    page.enter_password_confirm(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Длина пароля должна быть не менее 8 символов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(21)), (cyrill(22)), (spec_symb(255)), (digits(256)),
                          (latin(300) + latin(100).upper() + spec_symb(300) + digits(300))],
                         ids=['21 latin letters', '22 cyrillic letters', '255 spec.symbols', '256 digits',
                              '400 latin letters (100 upper) + 300 spec.symbols + 300 digits'])
def test_password_confirm_field_wrong_long(input_):
    page = RegPage()
    page.enter_password_confirm(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Длина пароля должна быть не более 20 символов')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(cyrill(8)), (cyrill(5) + latin(4)), (cyrill(12) + digits(7)),
                          (cyrill(15) + spec_symb(5)), (cyrill(8) + digits(2) + spec_symb(3))],
                         ids=['8 cyrillic letters', '5 cyrillic letters + 4 latin letters',
                              '12 cyrillic letters + 7 digits', '15 cyrillic letters + 5 spec.symbols',
                              '8 cyrillic letters + 2 digits + 3 spec.symbols '])
def test_password_confirm_field_wrong_cyrill(input_):
    page = RegPage()
    page.enter_password_confirm(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath", "//span[contains(text(), 'Пароль должен содержать только латинские буквы')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(8)), (latin(9).upper()), (latin(15) + latin(1).upper()),
                          (latin(1) + latin(19).upper())],
                         ids=['8 latin letters', '9 latin upper letters',
                              '16 latin letters (1 upper)', '20 latin letters (19 upper)'])
def test_password_confirm_field_wrong_without_dig_specsymb(input_):
    page = RegPage()
    page.enter_password_confirm(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath",
                            "//span[contains(text(), 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(7) + digits(1)), (latin(19) + spec_symb(1)), (latin(14) + digits(2) + spec_symb(3)),
                          (digits(12)), (spec_symb(9)), (digits(8) + spec_symb(6))],
                         ids=['7 latin letters + 1 digit', '19 latin letters + 1 spec.symbol',
                              '14 latin letters + 2 digits + 3 spec.symbols', '12 digits', '9 spec.symbols',
                              '8 digits + 6 spec.symbols'])
def test_password_confirm_field_wrong_without_upper(input_):
    page = RegPage()
    page.enter_password_confirm(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath",
                            "//span[contains(text(), 'Пароль должен содержать хотя бы одну заглавную букву')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result


@pytest.mark.parametrize('input_',
                         [(latin(4).upper() + digits(2) + spec_symb(2)), (latin(7).upper() + digits(7)),
                          (latin(2).upper() + spec_symb(18))],
                         ids=['4 latin upper letters + 2 digit + 2 spec.symbols', '7 latin upper letters + 7 digits',
                              '2 latin upper letters + 18 spec.symbols'])
def test_password_confirm_field_wrong_without_lower(input_):
    page = RegPage()
    page.enter_password_confirm(input_)
    page.name_click()

    try:
        page.driver.find_element("xpath",
                            "//span[contains(text(), 'Пароль должен содержать хотя бы одну строчную букву')]")
    except Exception as NoSuchElementException:
        result = True
    else:
        result = False
    finally:
        page.driver.refresh()
    assert not result
