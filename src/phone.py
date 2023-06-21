from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__name = name
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __repr__(self):
        super().__repr__()
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        """Сложение экземпляров класса по количеству товара в магазине"""
        super().__add__(other)
        if not isinstance(other, Phone) and not isinstance(other, Item):
            raise ValueError('Нельзя сложить Phone или Item с экземплярами не Phone или Item классов')
        return self.quantity + other.quantity
