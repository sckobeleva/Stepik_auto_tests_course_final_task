from .base_page import BasePage # импортируем BasePage, чтобы создать свой наследуемый от него класс

class MainPage(BasePage):   # объявляем класс главной страницы
    def __init__(self, *args, **kwargs):    # методов здесь не осталось, поэтому оставляем заглушку
        super(MainPage, self).__init__(*args, **kwargs)


