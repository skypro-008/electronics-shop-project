from src.item import Item


class MixinLang:
    __lang = "EN"


    @property
    def language(self):
        return self.__lang

    def change_lang(self):
        if self.__lang == "EN":
            self.__lang = "RU"
        else:
             self.__lang = "EN"
             return self

class KeyBoard(MixinLang, Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)




keyboard = KeyBoard('Logitech Wireless MX Keys Mini', 1600, 10)
print(keyboard)
