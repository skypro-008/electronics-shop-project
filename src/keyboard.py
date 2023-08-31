from src.item import Item


class MixinLanguage:
    Languages = ("EN", "RU")

    def __init__(self):
        self.__language = self.Languages[0]

    def change_lang(self):
        if self.__language == self.Languages[0]:
            self.__language = self.Languages[1]
        else:
            self.__language = self.Languages[0]

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        raise AssertionError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, MixinLanguage):

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
