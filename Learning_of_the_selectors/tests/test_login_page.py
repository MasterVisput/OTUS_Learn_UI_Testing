from Learning_of_the_selectors.pages.base_page import BasePage
from Learning_of_the_selectors.pages.selectors import LoginPageSelectors


def test_button_continue_is_presents(browser, url):
    page = BasePage(browser, url+'/index.php?route=account/login')
    page.open()
    assert page.is_element_present(*LoginPageSelectors.BUTTON_CONTINUE), 'Элемент не найден на странице!'


def test_button_login_is_presents(browser, url):
    page = BasePage(browser, url+'/index.php?route=account/login')
    page.open()
    assert page.is_element_present(*LoginPageSelectors.BUTTON_LOGIN), 'Элемент не найден на странице!'


def test_email_field_is_presents(browser, url):
    page = BasePage(browser, url+'/index.php?route=account/login')
    page.open()
    assert page.is_element_present(*LoginPageSelectors.E_MAIL_FIELD), 'Элемент не найден на странице!'


def test_password_field_is_presents(browser, url):
    page = BasePage(browser, url+'/index.php?route=account/login')
    page.open()
    assert page.is_element_present(*LoginPageSelectors.PASSWORD_FIELD), 'Элемент не найден на странице!'


def test_forgotten_passwod_link_is_presents(browser, url):
    page = BasePage(browser, url+'/index.php?route=account/login')
    page.open()
    assert page.is_element_present(*LoginPageSelectors.FORGOTTEN_PASSWORD_LINK), 'Элемент не найден на странице!'