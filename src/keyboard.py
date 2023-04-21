from src.item import Item


class MixinLanguage:
    def __init__(self):
        self.__language = "EN"

    def get_lang(self):
        return self.__language

    def change_lang(self):
        self.__language = "RU" if self.__language == "EN" else "EN"
        return self


class Keyboard(Item, MixinLanguage):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

        MixinLanguage.__init__(self)

    @property
    def language(self):
        return self.get_lang()
