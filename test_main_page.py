from .pages.main_page import MainPage   # импортируем класс, элементы которого будем использовать в проверках
from .pages.login_page import LoginPage # импортируем класс, элементы которого будем использовать в проверках


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.should_be_login_link()     # выполняем метод страницы - проверяем, что есть ссылка логина или регистрации


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)    # используем конструкцию перехода на страницу, создаем объект login_page
    login_page.should_be_login_page()  # теперь мы можем использовать в этом же тесте методы LoginPage, а не только MainPage


def test_login_or_register_url(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.should_be_login_url()      # выполняем метод страницы - переходим на страницу логина


def test_guest_can_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_form()      # выполняем метод страницы - проверяем, что есть форма логина


def test_guest_can_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                        # открываем страницу
    page.should_be_register_form()   # выполняем метод страницы - проверяем, что есть форма регистрации


