from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        try:
            if 1 <= value == int(value):
                self.__number_of_sim = value
                return self.__number_of_sim
            else:
                raise ValueError
        except ValueError:
            print("Должно быть целым числом и больше нуля")
            return self.__number_of_sim

    def __repr__(self):
        super().__repr__()
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, {self.quantity}, {self.__number_of_sim})"
