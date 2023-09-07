from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, count_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.count_of_sim = count_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.count_of_sim})"

    def __str__(self):
        return f"{self.name}"
