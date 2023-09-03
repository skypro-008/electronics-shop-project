from src.item import Item
from src.item import LanguageMixin


class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
