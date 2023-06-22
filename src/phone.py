from src.item import Item


class Phone(Item):
    """
    Класс для представления смартфона в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.
        :param name: Название смартфона.
        :param price: Цена за единицу смартфона.
        :param quantity: Количество смартфонов в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = None  # Используем None вместо 0 по умолчанию
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value >= 0:  # Разрешаем 0
            self._number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше или равно нулю.")

    def __add__(self, other):
        """
        Оператор сложения для объектов Phone и Item.
        :param other: Другой объект, который нужно сложить с текущим объектом Phone.
        :return: Общее количество товара.
        """
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError(f"Нельзя сложить Phone и {type(other)}")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
