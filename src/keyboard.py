from src.item import Item


class MixinKeyboard:
    lang = "EN"
    @classmethod
    def change_lang(cls):
        if cls.lang == "EN":
             cls.lang = "RU"
        else:
             cls.lang = "EN"
        return cls.lang


class Keyboard(Item, MixinKeyboard):
    def __init__(self,name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = self.lang

    @property
    def language(self):
        return self._language

    def change_lang(self):
        super().change_lang()
        self._language = self.lang
        return self