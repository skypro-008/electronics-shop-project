from src.item import Item


class MixinLang:

    def __init__(self,  language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        self.__language = 'RU' if self.__language == 'EN' else 'EN'
        return self


class Keyboard(Item, MixinLang):

    def __init__(self, name, price, amount, language='EN'):
        super().__init__(name, price, amount)
        MixinLang.__init__(self, language)
