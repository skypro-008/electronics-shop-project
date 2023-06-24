from src.item import Item


class MixinLang:
    base_language = "EN"

    def __init__(self):
        self.__language = MixinLang.base_language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
