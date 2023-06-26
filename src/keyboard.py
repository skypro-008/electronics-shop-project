from src.item import Item


class MixinLang:
    """Класс для хранения и изменения раскладки клавиатуры"""
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        elif self.__language == 'RU':
            self.__language = 'EN'
            return self


class Keyboard(Item, MixinLang):
    pass
