from src.item import Item

class Phone(Item):
    """
    Класс телефонов с сим-картами
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_simkards: int):
        super().__init__(name, price, quantity)
        self.__number_of_simkards = number_of_simkards

    @property
    def number_of_simkards(self):
        """
        геттер для сим
        """
        return self.__number_of_simkards


    @number_of_simkards.setter
    def number_of_simkards(self, num_of_sim):
        """
        сеттер для сим
        """
        if not isinstance(num_of_sim, int) or num_of_sim <= 0:
            raise ValueError('Количество сим должно быть целым положительным числом')
        self.__number_of_simkards = num_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}', {self.price}, {self.quantity}, {self.number_of_simkards})"

    def __str__(self):
        return f"{self.name}"

