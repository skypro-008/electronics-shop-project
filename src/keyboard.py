from src.item import Item


class MixinLog:

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, data):
        self.__language = data
        if self.__language != "EN" or self.__language != "RU":
            raise AttributeError("AttributeError: property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)



kb = Keyboard('Dark Project KD87A', 9600, 5)

kb.language
