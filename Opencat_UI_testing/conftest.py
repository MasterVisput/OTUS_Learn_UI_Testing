import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from Opencat_UI_testing.pages.product_page import ProductPage


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='Chrome',
        help='This is browser for testing'
    )
    parser.addoption(
        '--url',
        action='store',
        default='http://localhost/',
        help='This is url for testing'
    )


@pytest.fixture
def browser_opt(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def browser(browser_opt):
    if browser_opt == 'Chrome':
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(options=options)
    elif browser_opt == 'Firefox':
        options = FirefoxOptions()
        options.add_argument('--kiosk')
        browser = webdriver.Firefox(options=options)
        profile.accept_untrusted_certs = True
    elif browser_opt == 'IE':
        browser = webdriver.Ie()
    yield browser
    browser.quit()
