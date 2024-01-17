from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Магические методы __repr__
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """
        Магические методы __add__ сложение и проверка принадлежность к классу
        """
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            raise ValueError("Нельзя сложить классы 'Phone' или 'Item' с не 'Phone' или 'Item'")

    @property
    def number_of_sim(self):
        """
        Геттер количества сим-карт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        """
        Сеттер количества сим-карт больше 0
        """
        if new_number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = new_number_of_sim

###########################