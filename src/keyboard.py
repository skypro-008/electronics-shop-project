from src.item import Item


class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "RU":
            self.__language = "EN"
        else:
            self.__language = "RU"
