import pytest   # импортируем питест, чтобы не ругалось на фикстуру
from .pages.product_page import ProductPage # импортируем класс, элементы которого будем использовать в проверках
from .pages.basket_page import BasketPage   # импортируем класс, элементы которого будем использовать в проверках

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])   # фикстура с параметризацией, одним тестом прогоням 9 ссылок с началом link и концом 0,1 и т.д.
# на ссылке с параметром "?promo=offer7" тест падает и его не будут фиксить, поэтому помечаем как XFail (ожидаемо падающий)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.should_not_be_success_message() # проверяем, что пока нет хинта и добавлении товара в корзину
    page.click_btn_add_to_basket()  # нажимаем добавить в корзину
    page.solve_quiz_and_get_code()  # считаем результат и вставляем в алерт
    page.should_be_success_message()    # проверяем, что есть хинт о добавлении товара в корзину
    page.should_be_correct_name_in_message()    # проверяем, что в хинте правильное наименование товара
    page.should_be_correct_price_in_message()   # проверяем, что в хинте правильная цена

@pytest.mark.xfail  # тест упадет, помечаем как ожидаемо падающий
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.click_btn_add_to_basket()    # добавляем товар в корзину
    page.should_not_be_success_message()    # gроверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.should_not_be_success_message()   # проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.xfail  # тест упадет, помечаем как ожидаемо падающий
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/" # открываем страницу товара
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.click_btn_add_to_basket()    # добавляем товар в корзину
    page.success_message_should_be_disappeared()    # проверяем, что нет сообщения об успехе с помощью is_disappeared


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() # проверяем, что видим ссылку для регистрации


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page() # проверяем, что можем перейти на страницу регистрации


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу товара
    page.go_to_basket() # переходим в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)  # используем конструкцию перехода на страницу, создаем объект login_page
    basket_page.total_amount_should_be_null()    # ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_message()    # ожидаем, что есть текст о том что корзина пуста

