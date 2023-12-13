from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, i):
        """
        выдает ошибку если number_of_sim не равен 0
        """
        if isinstance(i, int) and i > 0:
            self.__number_of_sim = i
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
