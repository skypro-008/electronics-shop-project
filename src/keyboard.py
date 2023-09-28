from src.item import Item


class KeyboardMixin:
    """
    Класс для увеличения функциональности объектов класса Keyboard.
    Будет участвовать в наследовании как базовый класс
    :param language: Язык клавиатуры.
    """
    def __init__(self):
        """
        Инициализация класса миксин
        :param language: Язык клавиатуры - по умолчанию - 'EN'
        """
        self.__language = 'EN'

    @property
    def language(self):
        """
        Метод геттер для свойства language
        """
        return self.__language

    def change_lang(self):
        """
        Метод для смены языка раскладки клавиатуры
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self.__language


class Keyboard(Item, KeyboardMixin):
    """
    Класс для представления товара - 'клавиатура'
    Наследуется от класса Item
    Содержит дополнительный атрибут:
    """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)


    def __str__(self):
        """
        Магический метод для удобочитаемой строки для пользователя
        """
        return self.name


