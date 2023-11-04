from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if isinstance(number, int) and number > 0:
            self.__number_of_sim = number
        else:
            raise ValueError('Сим-карт не может быть отрицательное количество')

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
        )
