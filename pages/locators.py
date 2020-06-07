from selenium.webdriver.common.by import By # импортируем, чтобы писать селекторы


class BasePageLocators():   # объявляем класс селекторов, одинаковых для всех страниц
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini [class = 'btn btn-default']")

class LoginPageLocators():  # объявляем класс селекторов для элементов страницы логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():    # объявляем класс селекторов для элементов страницы с товаром
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) .alertinner")
    NAME_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6 h1")
    NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-safe:nth-child(1) .alertinner strong")
    PRICE_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-safe:nth-child(3) .alertinner strong")


class BasketPageLocators():  # объявляем класс селекторов для элементов корзины
    TOTAL_AMOUNT = (By.CSS_SELECTOR, ".col-sm-2 p")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
