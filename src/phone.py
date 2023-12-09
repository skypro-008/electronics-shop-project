from src.item import Item


class Phone(Item):
    def __init__(self, name, price: float, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.verify_sim(number_of_sim)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return (f"{__class__.__name__}('{str(self.name)}', {str(self.price)},"
                f" {str(self.quantity)}, {str(self.__number_of_sim)})")

    @classmethod
    def verify_sim(cls, __number_of_sim):
        if not isinstance(__number_of_sim, int) or __number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        self.verify_sim(number_of_sim)
        self.__number_of_sim = number_of_sim
