from src.item import Item

class Phone(Item):

    def __init__(self, name: str, price: int, quantity: int, number_simcards: int):
        super().__init__(name, price, quantity)
        self.number_simcards = number_simcards

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_simcards})"

    @property
    def number_of_sim(self):
        return self.number_simcards

    @number_of_sim.setter
    def number_of_sim(self, date):
        if date <= 0:
            raise ValueError ("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self.number_simcards = date