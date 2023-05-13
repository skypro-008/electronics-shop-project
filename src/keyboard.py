from src.item import Item

class KeyboardMixing:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "RU":
            self.__language = "EN"
        else:
            self.__language = "RU"


class Keyboard(Item, KeyboardMixing):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        KeyboardMixing.__init__(self)


