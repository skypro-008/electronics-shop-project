from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, count_of_sim: int) -> None:
        super().__init__(self, name, price, quantity)
        self.count_of_sim = count_of_sim
