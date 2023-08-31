from src.item import Item
class Mixin:
    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class Keyboard(Item, Mixin):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self._language = language

    def __str__(self):
        return self.name

    @property
    def language(self):
        return self._language

