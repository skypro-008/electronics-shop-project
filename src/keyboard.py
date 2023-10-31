from src.item import Item


class MixinLog:
    lang = 'EN'

    def __init__(self):
        self._language = 'EN'
        MixinLog.language = self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)


    @property
    def language(self):
        return self._language


