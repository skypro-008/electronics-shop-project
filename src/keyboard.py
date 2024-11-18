from src.item import Item


class LanguageMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._language = "EN"

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(LanguageMixin, Item):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
