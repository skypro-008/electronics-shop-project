from src.item import Item


class Phone(Item):
    def __init__(self, name, price, amount, number_of_sim):
        super().__init__(name, price, amount)
        self.__name = name
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.amount}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_cards):
        if sim_cards > 0 and isinstance(sim_cards, int):
            self._number_of_sim = sim_cards
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
