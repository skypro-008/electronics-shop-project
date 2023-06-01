from src.item import Item


class MixinLang:
    __language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLang):
    pass