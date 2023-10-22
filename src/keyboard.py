from src.item import Item


class MixinLog:

    def __init__(self):
        language = 'EN'
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language
        if self.language != "EN" and self.language != "RU":
            raise ValueError

    def __str__(self):
        return f'{self.name}'


