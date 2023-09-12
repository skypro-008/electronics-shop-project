# -*- coding: utf-8 -*-
from src.item import Item

class MixinLanguage:
    """
    Класс-миксин, который “подмешивается” в цепочку наследования класса `Keyboard`, который имеет
    дополнительный функционал по хранению и изменению раскладки клавиатуры.
    """
    def __init__(self, language="EN"):
        """
        Инициализация языка по умолчанию - английский
        """
        self.__language = language

    @property
    def language(self):
        """
        Выводит раскладку клавиатуры
        """
        return self.__language

    def change_lang(self):
        """
        Изменяет раскладку клавиатуры
        """
        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
        return self

class Keyboard(Item, MixinLanguage):
    """
    Класс  для товара “клавиатура” - дочерний класс Item
    """
    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN'):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self, language)
