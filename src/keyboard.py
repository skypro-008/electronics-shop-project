from src.item import Item

class Mixinlanguage:
    LANGUAGE = "EN"

    def __init__(self):
        self.__language = self.LANGUAGE

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self
        self.__language = "EN"
        return  self

    @property

    def language(self):
        return self.__language

    @language.setter
    def language(self,lang):
        if lang not in ["EN", "RU"]:
            raise  AttributeError("property 'language' of 'KeyBoard' object has no setter")
        self.__language = lang


class Keyboard(Item, Mixinlanguage):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)




