from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int = 1):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Phone) or isinstance(other, Item):
            return self.quantity + other.quantity

        elif isinstance(other, int):
            return self.quantity + other

        else:
            return "Телефон можно складывать только с числами!"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
