from src.item import Item


class Mixin:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, i):
        """
        выдает ошибку если language не русский и не английсний
        """
        if i != "EN" and i != "RU":
            raise ValueError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        """
        При вызове меняет язык
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, Mixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)
