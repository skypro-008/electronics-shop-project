from src.item import Item
from src.mixin_langauge import LanguageMixin


class Keyboard(Item, LanguageMixin):
    max_name = 20

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._langauge_list = ['EN', 'RU']
        self._index = 0
