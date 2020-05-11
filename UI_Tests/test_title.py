
class TestOpencard():

    def test_title(self, browser, url):
        browser.get(url)
        assert browser.title == 'Your Store', 'Некорретное название страницы'
