from src.item import Item


class KeyboardLayoutMixin:
    def __init__(self):
        self._layout = "EN"

    def change_lang(self):
        if self._layout == "EN":
            self._layout = "RU"
        else:
            self._layout = "EN"

    @property
    def layout(self):
        return self._layout


class Keyboard(Item, KeyboardLayoutMixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        KeyboardLayoutMixin.__init__(self)

    @property
    def language(self):
        return self.layout

    @language.setter
    def language(self, new_lang):
        if new_lang in ("EN", "RU"):
            self._layout = new_lang
        else:
            raise ValueError("property 'language' of 'Keyboard' object has no setter")
