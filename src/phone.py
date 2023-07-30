from item import Item


class Phone(Item):
    """
    Создание экземпляра класса Phone
    """
    def __init__(self, name: str, price: float, quantity: int, sim_card: int):
        super().__init__(name, price, quantity)
        self.sim_card = sim_card
