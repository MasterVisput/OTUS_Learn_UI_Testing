from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()