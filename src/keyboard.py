from src.item import Item


class MixinLog:

    Language = "EN"

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = self.Language

    def change_lang(self):
        if self.__language == "EN":
            MixinLog.Language = "RU"
            self.__language = MixinLog.Language
            return self
        elif self.__language == "RU":
            MixinLog.Language = "EN"
            self.__language = MixinLog.Language
            return self

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLog, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
