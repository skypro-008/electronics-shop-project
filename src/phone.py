from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Реализация сеттера для функции number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Реализация геттера для функции number_of_sim"""
        if value <= 0:

            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = value

    def __repr__(self):
        """Метод вывода новый"""
        parent_repr = super().__repr__()
        return f"{parent_repr.split(',')[0]}, {self.price}, {self.quantity}, {self.__number_of_sim})"
