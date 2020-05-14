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

def test_admin_login(browser, url):
    page = BasePage(browser, url+'/admin/')
    page.open()
    page.login_admin()
    assert browser.title == 'Dashboard', 'Не удалось перейти на страницу администрирования'

def test_logout(browser, url):
    page = BasePage(browser, url+'/admin/')
    page.open()
    page.login_admin()
    page = BasePage(browser, browser.current_url)
    title = page.log_out()
    assert title == 'Administration', f'Не удалось выполнить логаут, ош: {title}'


def test_products_tab(browser, url):
    page = BasePage(browser, url+'/admin/')
    page.open()
    page.login_admin()
    page = BasePage(browser, browser.current_url)
    products_tab = page.open_product_tab()
    assert type(products_tab) is list, 'Таблица с продуктами на странице не найдена'







