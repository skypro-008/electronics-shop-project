from src.item import Item


class Phone(Item):
    """
    Класс для представления телефонов в магазине, созданный от класса Item.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self._number_of_sim = number_of_sim

    def __repr__(self):
        """Возвращает информацию о классе по шаблону <Phone(name, price, quantity, number_of_sim)>"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self._number_of_sim = number_of_sim
