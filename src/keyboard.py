from src.item import Item


class MixinLang:
    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'

        return self


class Keyboard(Item, MixinLang):
    def change_lang(self):
        return MixinLang.change_lang(self)
