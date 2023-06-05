from src.item import Item


class Keyboard(Item):
    def __init__(self,name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language


    def change_lang(self):
        if self.language == "EN":
            self._language = "RU"
            return self
        else:
            self._language = "EN"
            return self

