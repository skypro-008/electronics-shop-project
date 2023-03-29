from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim: int):
        super().__init__(name, price, quantity)
        self.__sim = sim

    @property
    def sim(self):
        return self.__sim

    @sim.setter
    def sim(self, value: int):
        try:
            if 1 <= value == int(value):
                self.__sim = value
            else:
                raise ValueError
        except ValueError:
            print("Должно быть целым числом и больше нуля")
            return self.__sim

    def __repr__(self):
        super().__repr__()
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, {self.quantity}, {self.__sim})"
