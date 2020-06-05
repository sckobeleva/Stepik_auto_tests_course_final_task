from .base_page import BasePage # импортируем BasePage, чтобы создать свой наследуемый от него класс
from .locators import MainPageLocators # импортируем класс локаторов, чтоб применить их в проверках


class MainPage(BasePage):   # объявляем класс главной страницы
    def go_to_login_page(self): # переходим на страницу логина
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)    # находим элемент
        login_link.click()  # кликаем по нему

    def should_be_login_link(self): # Проверяем наличие ссылки для логина или регистрации
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

