from src.item import Item


class MixinLang:
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        def __init__(self):
            self._language = "EN"

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == "EN":
             self._language = "RU"
        else:
             self._language = "EN"
             return self

class KeyBoard(MixinLang, Item):
    pass


keyboard = KeyBoard('Logitech Wireless MX Keys Mini', 1600, 10)
print(keyboard)
