from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"('{self.name}', {self.price}, " \
               f"{self.quantity}, {self.number_of_sim })"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, add_number_of_sim):
        if int(add_number_of_sim) > 0:
            self.__number_of_sim = int(add_number_of_sim)

        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
