from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        """
        Инициализируем класс Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Добавляем магический метод __repr__
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """
        Добавляем магический метод __str__
        """
        return self.name

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        self.__number_of_sim = value
        if not isinstance(value, int) or value <= 0:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
