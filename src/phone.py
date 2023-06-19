from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if 0 < number_of_sim == int(number_of_sim):
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Number of sim must be positive and int type')
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if 0 < number_of_sim == int(number_of_sim):
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Number of sim must be positive and int type')
