from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote as RemoteWebDriwer
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Opencat_UI_testing.pages.selectors import LoginAdminPageSelector, DashboardPageSelectors, AddNewProductCartSelectors


class BasePage():
    def __init__(self, browser: RemoteWebDriwer, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        weit = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((how, what)))
        elements_lst = self.browser.find_elements(how, what)
        if len(elements_lst) == 0:
            return False
        else:
            return True

    def login_admin(self):
        username_field = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(LoginAdminPageSelector.USERNAME_FIELD))
        username_field.send_keys('user')
        password_field = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(LoginAdminPageSelector.PASSWOD_FIELD))
        password_field.send_keys('bitnami1')
        login_button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(LoginAdminPageSelector.LOGIN_BUTTON))
        login_button.click()
        try:
            weit = WebDriverWait(self.browser, 5).until(EC.title_contains('Dashboard'))
            return self.browser.title
        except TimeoutException:
            return 'TimeoutException'

    def log_out(self):
        logout_link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(DashboardPageSelectors.LOGOUT_LINK))
        logout_link.click()
        try:
            weit = WebDriverWait(self.browser, 5).until(EC.title_contains('Administration'))
            return self.browser.title
        except TimeoutException:
            return 'TimeoutException'

    def open_product_tab(self):
        weit = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(DashboardPageSelectors.CATALOG_LINK))
        catalog_link = self.browser.find_elements(*DashboardPageSelectors.CATALOG_LINK)
        catalog_link[0].click()
        product_link = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(DashboardPageSelectors.PRODUCT_LINK))
        product_link.click()
        try:
            products_tab = WebDriverWait(self.browser, 5).until(
                EC.presence_of_all_elements_located(DashboardPageSelectors.PRODUCT_TAB))
            return products_tab
        except TimeoutException:
            return 'TimeoutException'



