from src.item import Item


class MixinLanguage:

    def __init__(self, language='EN'):
        self.language = language

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
            return self
        else:
            self.language = 'EN'
            return self

    # @property
    # def language(self):
    #     return self.language


class KeyBoard(Item, MixinLanguage):
    
    def __init__(self, *args):
        super().__init__(*args)



    def __str__(self):
        return super().__str__()
