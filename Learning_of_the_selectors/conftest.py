from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        action='store',
        default='http://localhost',
        help='This is url for testing'
    )


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
