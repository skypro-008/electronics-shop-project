from src.item import Item


class MixinLog:
    __language = 'EN'
    keyboard_lang = []

    def __init__(self):
        self.keyboard_lang = []

    def add_to_keyboard_lang(self, value):
        self.keyboard_lang.append(value)

    @property
    def language(self):
        return self.__language

    # @property
    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            MixinLog.add_to_keyboard_lang(MixinLog, self.__language)
        else:
            self.__language = 'EN'
            MixinLog.add_to_keyboard_lang(MixinLog, self.__language)


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self):
        return f'{self.name}'
