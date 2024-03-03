from src.item import Item


class Mixin:
    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, Mixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)
