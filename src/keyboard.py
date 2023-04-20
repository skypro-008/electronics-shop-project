from src.item import Item


class MixinKeyLang:
    """Класс миксин для ввода раскладки клавиатуры"""
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        self.language = "RU"
        return self.language

class KeyBoard(Item, MixinKeyLang):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

