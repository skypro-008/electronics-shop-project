from item import Item


class MixinLog:

    def __init__(self, name, price, quantity, language):
        super().__init__(name, price, quantity, language)
        if self.language != 'EN' or self.language != 'RU':
            raise AttributeError

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language

    def __str__(self):
        return self.name
