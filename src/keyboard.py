from src.item import Item

class Mixinkey():
    def __init__(self):
        self.__language = "EN"
    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if  self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, Mixinkey):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        Mixinkey.__init__(self)
