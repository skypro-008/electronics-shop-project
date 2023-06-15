from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            return None
        return self.quantity + other.quantity

