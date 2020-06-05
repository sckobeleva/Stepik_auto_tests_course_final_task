import pytest   # импортируем питест, чтобы не ругалось на фикстуру
from .pages.product_page import ProductPage # импортируем класс, элементы которого будем использовать в проверках


@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])   # фикстура с параметризацией, одним тестом прогоням 9 ссылок с началом link и концом 0,1 и т.д.
# на ссылке с параметром "?promo=offer7" тест падает и его не будут фиксить, поэтому помечаем как XFail (ожидаемо падающий)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.click_btn_add_to_basket()  # нажимаем добавить в корзину
    page.solve_quiz_and_get_code()  # считаем результат и вставляем в алерт
    page.should_be_success_message()    # проверяем, что есть хинт о добавлении товара в корзину
    page.should_be_correct_name_in_message()    # проверяем, что в хинте правильное наименование товара
    page.should_be_correct_price_in_message()   # проверяем, что в хинте правильная цена

