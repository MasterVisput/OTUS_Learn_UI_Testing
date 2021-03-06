from selenium.webdriver.common.by import By


class CatalogPageSelectors():
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search > input')
    BASKET_BUTTON = (By.XPATH, '//*[@id="cart"]/button')
    GRID_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    LIST_BUTTON = (By.XPATH, '//*[@id="list-view"]')
    LINK_PRODUCT_COMPARE = (By.CSS_SELECTOR, '#compare-total')


class ProductCardSelectors():
    BUTTON_ADD_TO_WISH_LIST = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    QTY_FIELD = (By.CSS_SELECTOR, '#input-quantity')
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, '#button-cart.btn-lg')
    BUTTON_COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')
    REVIEWS_LINK = (By.CSS_SELECTOR, '[href="#tab-review"]')


class LoginPageSelectors():
    BUTTON_CONTINUE = (By.XPATH, '//a[text()="Continue"]')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[value="Login"]')
    E_MAIL_FIELD = (By.CSS_SELECTOR, '[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[name="password"]')
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, '.form-group a')

class LoginAdminPageSelector():
    USERNAME_FIELD = (By.CSS_SELECTOR, '[name="username"]')
    PASSWOD_FIELD = (By.CSS_SELECTOR, '[name="password"]')
    FORGOTTEN_PASSWORD = (By.XPATH, '//a[text()="Forgotten Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    OPENCART_LINK = (By.XPATH, '//a[text()="OpenCart"]')













