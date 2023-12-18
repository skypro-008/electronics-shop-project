from src.item import Item


class LanguageMixin:
    EN = 'EN'
    RU = 'RU'

    def __init__(self):
        self._language = self.EN

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == self.EN:
            self._language = self.RU
        else:
            self._language = self.EN


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)
