from src.item import Item

class Phone(Item):
    """
    Класс телефонов с сим-картами
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Невозможно сложить Phone или Item с экземплярами других классов")

    @property
    def number_of_sim(self):
        """
        геттер для сим
        """
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, num_of_sim):
        """
        сеттер для сим
        """
        if not isinstance(num_of_sim, int) and num_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = num_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.name}"

