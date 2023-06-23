from src.item import Item


class Keyboard(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = "EN"

