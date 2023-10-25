from src.item import Item


class MixinLang:

    def __init__(self,  language='EN'):
        self.language = language

    @property
    def language(self):
        return self.language

    def change_lang(self):
        self.language = 'RU' if self.language == 'EN' else 'EN'
        return self


class Keyboard(Item, MixinLang):

    def __init__(self, __name, price, amount, language='EN'):
        super().__init__(__name, price, amount)
        self.language = language

    def change_lang(self):
        self.language = super().change_lang()
        return self
