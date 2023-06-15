from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, count_sim):
        super().__init__(name, price, quantity)
        self.count_sim = count_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            return None
        return self.quantity + other.quantity

