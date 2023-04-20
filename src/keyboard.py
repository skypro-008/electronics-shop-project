from src.item import Item


class MixinKeyLang:
    """Класс миксин для ввода раскладки клавиатуры"""
    __slots__ = ('__language')
    def __init__(self):
        self.__language = "EN"
    @property
    def language(self):
        """Реализация сеттера для language"""
        return self.__language

    @language.setter
    def language(self, value):
        """Геттер для language"""
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter.")


    def change_lang(self):
        """метод смены раскладки клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self

class KeyBoard(Item, MixinKeyLang):
    """реализация класса KeyBoard, повторяющего функционал KeyBoard + миксин"""

    def __init__(self, *args):
        super().__init__(*args)

