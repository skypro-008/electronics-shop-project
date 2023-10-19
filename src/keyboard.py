from src.item import Item


class Keyboard(Item):
    __slots__ = ('EN', 'RU')

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.language = 'EN'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

    @property
    def change_lang(self):
        return self.language

    @change_lang.setter
    def change_lang(self, lang):
        if self.language == 'EN':
            self.language = 'EN'
            MixinLog.add_lang_in_list(MixinLog, self.language)
        elif self.language == 'RU':
            self.language = 'RU'
            MixinLog.add_lang_in_list(MixinLog, self.language)


class MixinLog:
    list_lang = []

    def __init__(self, list_lang):
        self.list_lang = list_lang

    def add_lang_in_list(self, lang):
        return self.list_lang.append(lang)


kb = Keyboard('Dark Project KD87A', 9600, 5)
print(repr(kb))
kb.language = "RU"
print(repr(kb))
kb.language = "CH"
print(repr(kb))


