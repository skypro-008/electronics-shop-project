from src.item import Item


class MixinLog:

    Language = "EN"

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = self.Language

    def change_lang(self):
        if self.language == "EN":
            MixinLog.Language = "RU"
            self.language = MixinLog.Language
            return self
        elif self.language == "RU":
            MixinLog.Language = "EN"
            self.language = MixinLog.Language
            return self


class Keyboard(MixinLog, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
