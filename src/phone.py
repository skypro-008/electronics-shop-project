from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim: int):
        super().__init__(name, price, quantity)
        self.__sim = sim