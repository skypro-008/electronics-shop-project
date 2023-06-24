from src.item import Item


class MixinLang:
    """Механизм смены языка"""

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = "EN"


    @property
    def language(self):
        return self.__language


    @language.setter
    def language(self, other_language):
        """Функция по инициализации языка"""
        if other_language == ["EN", "RU"]:
            self.__language = other_language
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")


    def change_lang(self):
        """Функция по возможности изменения языка"""
        if self.__language == "EN":
            self.__language = "RU"
            return self
        self.__language = "EN"


class KeyBoard(MixinLang, Item):


    """Товар - Клавиатура"""


    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)


    def __str__(self):
        return f'{self.name}'
