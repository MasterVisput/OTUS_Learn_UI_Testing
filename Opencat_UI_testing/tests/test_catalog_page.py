from Opencat_UI_testing.pages.base_page import BasePage
from Opencat_UI_testing.pages.selectors import CatalogPageSelectors


def test_search_field_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/category&path=20')
    page.open()
    assert page.is_element_present(*CatalogPageSelectors.SEARCH_FIELD), 'Элемент не найден на странице!'


def test_basket_button_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/category&path=20')
    page.open()
    assert page.is_element_present(*CatalogPageSelectors.BASKET_BUTTON), 'Элемент не найден на странице!'


def test_grid_button_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/category&path=20')
    page.open()
    assert page.is_element_present(*CatalogPageSelectors.GRID_BUTTON), 'Элемент не найден на странице!'


def test_list_button_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/category&path=20')
    page.open()
    assert page.is_element_present(*CatalogPageSelectors.LIST_BUTTON), 'Элемент не найден на странице!'


def test_link_product_compare_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/category&path=20')
    page.open()
    assert page.is_element_present(*CatalogPageSelectors.LINK_PRODUCT_COMPARE), 'Элемент не найден на странице!'
