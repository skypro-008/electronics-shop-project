from src.item import Item


class Mixin:
    """
    Класс содержащий информацию о языке клавиатуры
    """

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Функция для изменения языка клавиатуры
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(Item, Mixin):
    """
    Класс для товара "Клавиатура" содержащий название товара, цену, количество, товара
     и язык клавиатуры(по умолчанию язык английский)
    """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
