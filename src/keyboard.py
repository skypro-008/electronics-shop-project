from src.item import Item


class MixinLog:
    ENG = "EN"

    def __init__(self):
        self.__language = self.ENG

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value == "RU" or value == "EN":
            self.__language = value
        else:
            raise AttributeError

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self

class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

# s = MixinLog()
# s.language = "RU"
# print(s.language)

