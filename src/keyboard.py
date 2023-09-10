from src.item import Item


class MixinLog:
    ENG = "EN"

    def __init__(self):
        self.language = self.ENG

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self.language

    def get_language(self):
        return self.language


class Keyboard(Item, MixinLog):
    pass

# s = MixinLog()
# s.language = "RU"
# print(s.language)