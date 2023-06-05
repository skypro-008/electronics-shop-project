from src.item import Item


class MixinLang:
    __lang = 'EN'

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.__lang

    def change_lang(self):
        if self.__lang == 'EN':
            self.__lang = 'RU'
            return self
        else:
            self.__lang = 'EN'
            return self


class KeyBoard(MixinLang, Item):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


keyboard = KeyBoard('Logitech Wireless MX Keys Mini', 1600, 10)
