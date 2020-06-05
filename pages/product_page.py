from .base_page import BasePage # импортируем BasePage, чтобы создать свой наследуемый от него класс
from .locators import ProductPageLocators   # импортируем класс локаторов, чтоб применить их в проверках


class ProductPage(BasePage):
    def should_be_btn_add_to_basket(self):  # проверяем, что есть кнопка "Добавитть в корзину"
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'Add to basket' is not presented"

    def click_btn_add_to_basket(self):  # кликаем по кнопке "Добавитть в корзину"
        click_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        click_btn.click()

    def should_be_success_message(self): # проверяем, что есть хинт о добавлении товара в корзину
        message_element = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE) # находим элемент
        message = message_element.text  # извлекаем текст
        assert 'был добавлен в вашу корзину' or 'has been added to your basket' in message, "Message is not presented"  # сравниваем с нужным текстом

    def should_be_correct_name_in_message(self):    # проверяем, что название на странице товара и в хинте совпадает
        name1_element = self.browser.find_element(*ProductPageLocators.NAME_ON_PAGE)    # находим элемент на странице
        name1 = name1_element.text  # извлекаем текст
        name2_element = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET)  # находим элемент в хинте
        name2 = name2_element.text  # извлекаем текст
        assert name1 == name2, "Incorrect book's name"  # сравниваем два найденных значения

    def should_be_correct_price_in_message(self):   # проверяем, что цена на странице товара и в хинте совпадает
        price1_element = self.browser.find_element(*ProductPageLocators.PRICE_ON_PAGE)  # находим элемент на странице
        price1 = price1_element.text    # извлекаем текст
        price2_element = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)    # находим элемент в хинте
        price2 = price2_element.text    # извлекаем текст
        assert price1 == price2, "Incorrect book's price"   # сравниваем два найденных значения






