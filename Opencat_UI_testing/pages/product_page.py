from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Opencat_UI_testing.pages.base_page import BasePage
from Opencat_UI_testing.pages.selectors import AddNewProductCartSelectors, DashboardPageSelectors


class ProductPage(BasePage):

    def add_new_product(self, p_name='Mouse', m_tag='pereferi', model='M23-546S'):
        self.open_product_tab()
        add_new_product_button = self.browser.find_element(*DashboardPageSelectors.ADD_NEW)
        add_new_product_button.click()
        wait = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(AddNewProductCartSelectors.PRODUCT_NAME))
        product_name = self.browser.find_element(*AddNewProductCartSelectors.PRODUCT_NAME)
        product_name.send_keys(p_name)
        meta_tag = self.browser.find_element(*AddNewProductCartSelectors.META_TAG)
        meta_tag.send_keys(m_tag)
        self.browser.find_element(*AddNewProductCartSelectors.DATA_TAB).click()
        wait = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(AddNewProductCartSelectors.MODEL))
        model_field = self.browser.find_element(*AddNewProductCartSelectors.MODEL)
        model_field.send_keys(model)
        save_button = self.browser.find_element(*AddNewProductCartSelectors.SAVE_BUTTON)
        save_button.click()
        return self.open_product_tab()

    def delete_product_from_tab(self, p_name='Mouse'):
        tab = self.open_product_tab()
        checkbox = self.get_checkbox_by_product_name(tab, p_name)
        checkbox.click()
        delete_button = self.browser.find_element(*DashboardPageSelectors.DELETE)
        delete_button.click()
        confirm = self.browser.switch_to.alert
        confirm.accept()

    def is_element_in_tab(self, elements_list, p_name='Mouse'):
        wait = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(AddNewProductCartSelectors.EDIT_BUTTON))
        for el in elements_list:
            name = el.find_element_by_css_selector('tr td:nth-child(3)')
            if name.text == p_name:
                return True

        return False

    def get_checkbox_by_product_name(self, elements_list, p_name='Mouse'):
        wait = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(AddNewProductCartSelectors.EDIT_BUTTON))
        for el in elements_list:
            name = el.find_element_by_css_selector('tr td:nth-child(3)')
            if name.text == p_name:
                checkbox = el.find_element_by_css_selector('tr td:nth-child(1)')
                return checkbox

        return False

    def is_product_in_tab(self, p_name='Mouse'):
        self.browser.find_element(*DashboardPageSelectors.DASHBOARD_LINK).click()
        elements_list = self.open_product_tab()
        wait = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(AddNewProductCartSelectors.EDIT_BUTTON))
        product_name_field = self.browser.find_element(*DashboardPageSelectors.PRODUCT_NAME_FIELD)
        product_name_field.send_keys(p_name)
        filter_button = self.browser.find_element(*DashboardPageSelectors.FILTER_BUTTON)
        filter_button.click()
        wait = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(AddNewProductCartSelectors.EDIT_BUTTON))
        for el in elements_list:
            name = el.find_element_by_css_selector('tr td:nth-child(3)')
            if name.text == p_name:
                return True

        return False

    def edit_product_from_tab(self, p_name='Mouse'):
        tab = self.open_product_tab()
        edit_button = self.get_edit_button_by_product_name(tab, p_name)
        edit_button.click()
        product_name_field = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(AddNewProductCartSelectors.PRODUCT_NAME))
        product_name_field.send_keys('Mouse+21')
        save_button = self.browser.find_element(*AddNewProductCartSelectors.SAVE_BUTTON)
        save_button.click()
        confirm = self.browser.switch_to.alert
        confirm.accept()


    def get_edit_button_by_product_name(self, elements_list, p_name='Mouse'):
        wait = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(AddNewProductCartSelectors.EDIT_BUTTON))
        for el in elements_list:
            name = el.find_element_by_css_selector('tr td:nth-child(3)')
            if name.text == p_name:
                edit_button = el.find_element_by_css_selector('tr td:nth-child(8)')
                return edit_button
