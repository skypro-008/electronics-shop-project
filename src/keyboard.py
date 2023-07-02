from src.item import Item


class MixinLang:
    """Класс-Миксин, хранит и меняет раскладку на клавиатуре"""
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class KeyBoard(Item, MixinLang):
    """Класс клавиатура"""
    pass
