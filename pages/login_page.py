from .base_page import BasePage # импортируем BasePage, чтобы создать свой наследуемый от него класс
from .locators import LoginPageLocators # импортируем класс локаторов, чтоб применить их в проверках


class LoginPage(BasePage):  # объявляем класс страницы логина
    def should_be_login_page(self): # методы приведенные ниже, объединены в один (требовалось в задании)
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # проверяем корректность url, а именно наличие "login" в адресе
        assert "login" in self.browser.current_url, "'login' is not in current url"

    def should_be_login_form(self): # проверяем, что на странице есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):  # проверяем, что на странице есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):   # регистрируем нового пользователя
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)  # находим элемент
        email_field.send_keys(email)    # вставляем в поле значение переменной email
        password_field_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)  # находим элемент
        password_field_1.send_keys(password)    # вставляем в поле значение переменной password
        password_field_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)  # находим элемент
        password_field_2.send_keys(password)    # вставляем в поле значение переменной password
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)  # Находим кнопку регистрации
        register_button.click()     # кликаем по ней

