from src.item import Item


class MixinLog:
    ENG = "EN"

    def __init__(self):
        self.language = self.ENG

    def change_lang(self) -> str:
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self

    def get_language(self):
        return self.language


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

# s = MixinLog()
# s.language = "RU"
# print(s.language)

