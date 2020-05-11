from Learning_of_the_selectors.pages.base_page import BasePage
from Learning_of_the_selectors.pages.selectors import LoginAdminPageSelector


def test_username_field_is_presents(browser, url):
    page = BasePage(browser, url+'/admin/')
    page.open()
    assert page.is_element_present(*LoginAdminPageSelector.USERNAME_FIELD), 'Элемент не найден на странице!'


def test_password_field_is_presents(browser, url):
    page = BasePage(browser, url+'/admin/')
    page.open()
    assert page.is_element_present(*LoginAdminPageSelector.PASSWOD_FIELD), 'Элемент не найден на странице!'


def test_forgotten_password_is_presents(browser, url):
    page = BasePage(browser, url+'/admin/')
    page.open()
    assert page.is_element_present(*LoginAdminPageSelector.FORGOTTEN_PASSWORD), 'Элемент не найден на странице!'


def test_login_button_is_presents(browser, url):
    page = BasePage(browser, url+'/admin/')
    page.open()
    assert page.is_element_present(*LoginAdminPageSelector.LOGIN_BUTTON), 'Элемент не найден на странице!'


def test_opencart_link_is_presents(browser, url):
    page = BasePage(browser, url+'/admin/')
    page.open()
    assert page.is_element_present(*LoginAdminPageSelector.OPENCART_LINK), 'Элемент не найден на странице!'
