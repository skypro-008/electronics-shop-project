from src.item import Item


class LanguageMixin:

    __lang = "EN"

    @property
    def language(self):
        return self.__lang

    def change_lang(self):
        if self.__lang == "EN":
            self.__lang = "RU"
            return self
        else:
            self.__lang = "EN"
            return self


class Keyboard(LanguageMixin, Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
