from src.item import Item

class Mixin:


    def change_lang(self):
        if self.language == "EN":
            self._language = "RU"
            return self
        else:
            self._language = "EN"
            return self

class Keyboard(Item, Mixin):
    def __init__(self,name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language



