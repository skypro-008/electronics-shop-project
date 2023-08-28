from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        self.__number_of_sim = number_of_sim
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        if value > 0 and type(value) == int:
            self.__number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
