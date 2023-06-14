from src.item import Item


class Phone(Item):
    """Создание дочернего класса от Item"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self.__number_of_sim = value

    def __add__(self, other):
        """Общее количества товара в двух классах"""
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return Exception

    def __repr__(self):
        """Вывод информаций в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"