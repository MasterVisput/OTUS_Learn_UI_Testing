from Learning_of_the_selectors.pages.base_page import BasePage
from Learning_of_the_selectors.pages.selectors import ProductCardSelectors


def test_button_add_to_wl_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/product&path=57&product_id=49')
    page.open()
    assert page.is_element_present(*ProductCardSelectors.BUTTON_ADD_TO_WISH_LIST), 'Элемент не найден на странице!'


def test_qty_field_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/product&path=57&product_id=49')
    page.open()
    assert page.is_element_present(*ProductCardSelectors.QTY_FIELD), 'Элемент не найден на странице!'


def test_button_add_to_card_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/product&path=57&product_id=49')
    page.open()
    assert page.is_element_present(*ProductCardSelectors.BUTTON_ADD_TO_CARD), 'Элемент не найден на странице!'


def test_button_compare_this_product_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/product&path=57&product_id=49')
    page.open()
    assert page.is_element_present(*ProductCardSelectors.BUTTON_COMPARE_THIS_PRODUCT), 'Элемент не найден на странице!'


def test_reviews_link_is_presents(browser, url):
    page = BasePage(browser, url + '/index.php?route=product/product&path=57&product_id=49')
    page.open()
    assert page.is_element_present(*ProductCardSelectors.REVIEWS_LINK), 'Элемент не найден на странице!'
