from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, sim):
        super().__init__(name, price, quantity)
        self.sim = sim

    # def __str__(self):
    #     return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim})"

    @property
    def number_of_sim(self):
        return self.sim

    @number_of_sim.setter
    def number_of_sim(self, new_sim):
        if int(new_sim) > 0 and isinstance(new_sim, int):
            self.sim = int(new_sim)
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")