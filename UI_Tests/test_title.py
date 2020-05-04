

class TestOpencard():

    def test_title(self, browser):
        browser.get('http://localhost/')
        assert browser.title == 'Your Store', 'Некорретное название титла'
