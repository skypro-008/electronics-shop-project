from src.item import Item
from src.language_mixin import LanguageMixin


class Keyboard(Item, LanguageMixin):
    max_name_len = 20

    def __init__(self, name: str, price: float, quantity: int, **kwargs):
        super().__init__(name, price, quantity, langs_list=['EN', 'RU'], **kwargs)
