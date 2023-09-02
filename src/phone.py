from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Класс Phone содержит все атрибуты класса Item и дополнительно атрибут,
        содержащий количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Устанавливает значение физических SIM-карт
        """
        if value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __str__(self):
        """
        Метод, возвращает название товара
        """
        return self.name

    def __repr__(self):
        """
        Метод, отображает информацию
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"