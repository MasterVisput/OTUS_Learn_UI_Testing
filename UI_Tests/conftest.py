from selenium import webdriver
import pytest
from selenium.webdriver import ChromeOptions, FirefoxOptions


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
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
    elif browser_opt == 'Firefox':
        options = FirefoxOptions()
        options.add_argument('--kiosk')
        options.add_argument('--headless')
        browser = webdriver.Firefox(options=options)
    elif browser_opt == 'IE':
        browser = webdriver.Ie()
    yield browser
    browser.quit()




