from src.item import Item


class MixinLog:
    """класс `Keyboard` для товара “клавиатура”"""
    LANGUAGE = "EN"

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        # Добавили втрибут языка
        self.__language = self.LANGUAGE

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        # метод изменения языка

        if self.__language == "EN":
            self.__language = "RU"
            return self

        else:
            self.__language = "EN"
            return self


class KeyBoard(MixinLog, Item):

    def __repr__(self):

        return f"{self.__class__.__name__}('{self.name}', {self.price}" \
               f", {self.quantity})"
