from .base_page import BasePage # импортируем BasePage, чтобы создать свой наследуемый от него класс
from .locators import BasketPageLocators # импортируем класс локаторов, чтоб применить их в проверках


class BasketPage(BasePage):
    def total_amount_should_be_null(self):   # проверяем, что корзина пуста, и элемента с суммой нет
        assert self.is_not_element_present(*BasketPageLocators.TOTAL_AMOUNT), "Total amount isn't null"

    def should_be_empty_message(self):   # проверяем, что корзина пуста, и есть соответствующее сообщение
        message_element = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE)  # находим элемент
        message_text = message_element.text # извлекаем текст
        assert 'Your basket is empty' in message_text, "Empty message is not presented"  # сравниваем с нужным текстом
