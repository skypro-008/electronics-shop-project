from src.item import Item


class MixinLog:
    lang = 'EN'

    def __init__(self):
        self.language = 'EN'
        MixinLog.language = self.language

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)


    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, lang):
        if lang!='EN' and lang!='RU':
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self._language=lang