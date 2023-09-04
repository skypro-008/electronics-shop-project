from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        """
        Инициализация для класса Phone
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер для number_of_sim
        """

        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        """
        Сеттер для number_of_sim
        """
        self._number_of_sim = new_number

        if self._number_of_sim <= 0 or not isinstance(self._number_of_sim, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
