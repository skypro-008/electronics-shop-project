from src.item import Item


class MixinLog:
    def __init__(self, language='EN'):
        self._language = language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
            return self
        if self._language == 'RU':
            self._language = 'EN'
            return self




class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self._language = language

