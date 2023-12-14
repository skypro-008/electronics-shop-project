from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError("Неподдерживаемая операция ")

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f"Phone('{self.name}', {self.price}, "
                f"{self.quantity}, {self._number_of_sim})")

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество  SIM-карт должно быть целым числом")
        self._number_of_sim = value
