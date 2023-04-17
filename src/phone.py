from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    #def __repr__(self):
        """метод вывода"""

    #    return f"{super().__repr__(), self.number_of_sim}"




