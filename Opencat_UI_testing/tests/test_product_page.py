from Opencat_UI_testing.pages.product_page import ProductPage


def test_add_new_product(browser, url):
    # создаём экземпляр страницы
    page = ProductPage(browser, url + '/admin')
    # используем базовую функцию, тобы перейти на счтраницу логина
    page.open()
    # выполняем логин
    page.login_admin()
    # используем базовую функцию, чтобы добавить продукт с дефолтными данными
    page.add_new_product(p_name='Mouse', m_tag='pereferi', model='M23-546S')
    # получаем таблицу с продуками и проверяем что продукт в ней.
    assert page.is_product_in_tab(p_name='Mouse')


def test_delete_product_from_tab(browser, url):
    # создаём экземпляер страницы
    page = ProductPage(browser, url + '/admin')
    # переходим на страницу логина
    page.open()
    # выполняем логин
    page.login_admin()
    # проверяем, есть ли продукт с дефолтным именем в таблице
    if page.is_product_in_tab(p_name='Mouse'):
        # если продукт есть, удаляем используя базовую функцию
        page.delete_product_from_tab(p_name='Mouse')
    else:
        # если продукта нет, добавляем
        page.add_new_product(p_name='Mouse')
        # теперь он точно есть, удаляем продукт
        page.delete_product_from_tab(p_name='Mouse')
    # проверяем что продукта с дефолтным именем в таблице нет
    assert not page.is_product_in_tab(p_name='Mouse')


def test_edit_product_from_tab(browser, url):
    # создаём экземпляер страницы
    page = ProductPage(browser, url + '/admin')
    # переходим на страницу логина
    page.open()
    # выполняем логин
    page.login_admin()
    # проверяем, есть ли продукт с дефолтным именем в таблице
    if page.is_product_in_tab(p_name='Mouse'):
        # если продукт есть, удаляем используя базовую функцию
        page.edit_product_from_tab(p_name='Mouse')
    else:
        # если продукта нет, добавляем
        page.add_new_product(p_name='Mouse')
        # теперь он точно есть, удаляем продукт
        page.edit_product_from_tab(p_name='Mouse')
    # проверяем что продукта с дефолтным именем в таблице нет
    assert page.is_product_in_tab(p_name='Mouse+21')

