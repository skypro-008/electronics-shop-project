from src.item import Item


class Lang_change_Mixin:
    """класс `Keyboard` для товара “клавиатура”"""
    __LANGUAGE = "EN"

    @property
    def language(self):
        return self.__LANGUAGE

    def change_lang(self):
        # метод изменения языка

        if self.__LANGUAGE == "EN":
            self.__LANGUAGE = "RU"
            return self

        else:
            self.__LANGUAGE = "EN"
            return self


class KeyBoard(Lang_change_Mixin, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):

        return f"{self.__class__.__name__}('{self.name}', {self.price}" \
               f", {self.quantity})"
