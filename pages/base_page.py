import math
from selenium.common.exceptions import NoSuchElementException   # импортируем нужное исключение
from selenium.common.exceptions import NoAlertPresentException  # импортируем нужное исключение

class BasePage:

    def __init__(self, browser, url, timeout=10):   # конструктор с атрибутами класса
        self.browser = browser  # browser это функция, которая передается как параметр (см.confest.py), она запускает браузер и закрывает после всех тестов
        self.url = url  # ссылка
        self.browser.implicitly_wait(timeout) # команда для неявного ожидания со значением по умолчанию 10

    def is_element_present(self, how, what): # проверяем, есть ли элемент, с помощью 2х аргументов: КАК искать (css) и ЧТО (строка-селектор)
        try:    # используем конструкцию try/except, чтобы перехватывать исключение NoSuchElementException
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self): # открываем нужную страницу в браузере, используя get().
        self.browser.get(self.url)

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

