from selenium.webdriver import Remote as RemoteWebDriwer


class BasePage():
    def __init__(self, browser: RemoteWebDriwer, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        elements_lst = self.browser.find_elements(how, what)
        if len(elements_lst) == 0:
            return False
        else:
            return True
