from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """метод вывода / переопределение"""

        class_name = self.__class__.__name__
        return f"{class_name}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __add__(self, other):
        """метод сложения количества"""

        return self.quantity + other.quantity





