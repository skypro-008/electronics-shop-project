from src.item import Item

class MixinLanguage:
    def __init__(self, name, price, quantity, language="EN") -> None:
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = "EN"
            return self


class KeyBoard(MixinLanguage, Item):
    def __init__(self, name: str, price: int, quantity: int) -> None:
        super().__init__(name, price, quantity)
