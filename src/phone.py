from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, sim_card):
        """
        Инициализация для класса Phone
        """
        super().__init__(name, price, quantity)
        self.sim_card = sim_card

    def __repr__(self):

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_card})"

    # def __add__(self, other):
    #     """
    #     Сложение количества товара экземпляров классов Phone и Item
    #     """
    #     summ_ =