import pytest   # импортируем питест
from selenium import webdriver  # импортируем вебдрайвер
from selenium.webdriver.chrome.options import Options   # импортируем класс Options, чтобы затем указать язык браузера

def pytest_addoption(parser):   # во встроенную функцию pytest_addoption добавляем обработчик опции
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox") # через командную строку можно пережать параметр-браузер
    parser.addoption('--language', action='store', default="en", help="Choose language: ru, en, ... (etc.))")     # через командную строку можно пережать параметр-язык

@pytest.fixture(scope="function")   # Встроенная фикстура request, которая обрабатывает переданные данные
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        # browser.implicitly_wait(5)  # неявное ожидание, говорим WebDriver искать каждый элемент в течение 5 секунд
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
        # browser.implicitly_wait(5)  # неявное ожидание, говорим WebDriver искать каждый элемент в течение 5 секунд
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser   # финализатором закрываем браузер (после завершения теста, который вызывал фикстуру, выполнение продолжится со строки, следующей за строкой yield)
    print("\nquit browser..")
    
    browser.quit()
