from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        try:
            sim_number = int(number)
        except ValueError:
            raise ValueError(
                'Количество физических SIM-карт должно быть целым числом'
            )

        if sim_number <= 0:
            raise ValueError(
                'Количество физических SIM-карт должно быть больше нуля'
            )

        self.__number_of_sim = number

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Нельзя сложить экземпляры классов отличные от Item или Phone')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"