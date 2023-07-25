from src.item import Item


class MixinLang:
    lang = "EN"

    @classmethod
    def change_lang(cls):
        if cls.lang == "EN":
            cls.lang = "RU"
        else:
            cls.lang = "EN"
        return cls.lang


class Keyboard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int,):
        super().__init__(name, price, quantity)
        self.__language = self.lang

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        super().change_lang()
        self.__language = self.lang
        return self

