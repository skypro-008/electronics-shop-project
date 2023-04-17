from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """метод вывода "Phone('iPhone 14', 120000, 5, 2)"""

        module_name = "__main__"
        class_name = self.__class__.__name__
        return f"{class_name}('{self.__name}', {self.price}, {self.quantity} {self.number_of_sim})"




