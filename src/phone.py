from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, sim_card):
        super().__init__(name, price, quantity)
        self.sim_card = sim_card



