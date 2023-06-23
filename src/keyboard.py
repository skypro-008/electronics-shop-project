from src.item import Item


class KeyboardMixin:
    def __init__(self):
        self.language = 'RU'

    def change_lang(self):
        self.language = 'RU'
        return self


class Keyboard(Item, KeyboardMixin):
    """
    Класс для представления клавиатуры в магазине.
    """

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language
