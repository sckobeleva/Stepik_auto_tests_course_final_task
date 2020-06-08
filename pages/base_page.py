import math
from selenium.common.exceptions import NoSuchElementException   # импортируем для методов def is_element_present и is_not_element_present
from selenium.common.exceptions import NoAlertPresentException  # импортируем для метода def solve_quiz_and_get_code
from selenium.common.exceptions import TimeoutException # импортируем для метода is_disappeared
from selenium.webdriver.support.ui import WebDriverWait # импортируем для метода is_disappeared
from selenium.webdriver.support import expected_conditions as EC    # импортируем для метода is_disappeared
from .locators import BasePageLocators


class BasePage():   # методы в алфавитном порядке

    def __init__(self, browser, url, timeout=10):   # конструктор с атрибутами класса
        self.browser = browser  # browser это функция, которая передается как параметр (см.confest.py), она запускает браузер и закрывает после всех тестов
        self.url = url  # ссылка
        self.browser.implicitly_wait(timeout) # команда для неявного ожидания со значением по умолчанию 10

    def go_to_login_page(self): # переходим на страницу логина
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)    # находим кнопку регистраии/логина
        login_link.click()  # кликаем по ней

    def go_to_basket(self):  # переходим в корзину
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)  # находим кнопку перехода в корзину
        basket_link.click()  # кликаем по кнопке

    def is_element_present(self, how, what): # проверяем, есть ли элемент, с помощью 2х аргументов: КАК искать (css) и ЧТО (строка-селектор)
        try:    # используем конструкцию try/except, чтобы перехватывать исключение NoSuchElementException
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what): # проверяем, есть ли элемент, с помощью 2х аргументов: КАК искать (css) и ЧТО (строка-селектор)
        try:    # используем конструкцию try/except, чтобы перехватывать исключение NoSuchElementException
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4): # проверяем, что элемент исчезнет через 4 секунды
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):  # открываем нужную страницу в браузере, используя get().
        self.browser.get(self.url)

    def should_be_login_link(self): # Проверяем наличие ссылки для логина или регистрации
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):    # проверяем, что пользователь залогинен
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def solve_quiz_and_get_code(self):  # считаем математическое выражение и вставляем в алерт (код был дан на уроке)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

