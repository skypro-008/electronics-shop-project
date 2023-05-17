from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """Инициализация класса Телефон"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        """Вывод на печать"""
        return f"{self.name}"

    def __repr__(self):
        """Вывод на печать для разработчика"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        """Суммирование количество телефонов"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Объекты не из одного класса")

    def __radd__(self, other):
        """Суммирование количество телефонов с права"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Объекты не из одного класса")

    @property
    def number_of_sim(self) -> int:
        """Вывод количество сим карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, edit_number):
        """Установить количество сим карт"""
        if not isinstance(edit_number, int) or edit_number < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = edit_number
