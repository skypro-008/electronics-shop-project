from src.item import Item


class MixinLog:

    def __init__(self):
        language = 'EN'
        self.language = language

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language
        if self.language != "EN" and self.language != "RU":
            raise ValueError

    def __str__(self):
        return f'{self.name}'

    @property
    def language(self):
        return f"{self.language}"






