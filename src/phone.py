from src.item import Item


class Phone(Item):
    """
    Создан дочерний класс Phone класса Item
    дополнен атрибутом "number_of_sim" содержащим количество сим-карт, которое поддерживает смартфон
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        """
        Add функция для сложения экземпляров класса Phone и Item по общему количеству товара
        выдающая исключение Exception в случе если складываются не экземпляры классов Phone и Item
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception

    def __str__(self):
        """
        Метод возвращающий для пользователя название товара
        return: название товара
        """
        return self.name

    def __repr__(self):
        """
        Метод возвращающий для разработчика имя класса, название товара, цену, количество товара в магазине,
        и количество сим-карт, которое поддерживает смартфон
        return: имя класса ('название товара', цена товара, количество товара в магазине)
        """
        return str(f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})")

    @property
    def number_of_sim(self):
        """
        Геттер для чтения приватного атрибута "number_of_sim"
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count_sim):
        """
        Сеттер проверяющий количество сим-карт, которое поддерживает смартфон
        если количество сим-карт равно 0, то сеттер возвращает исключение:
        ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
        """
        if count_sim == 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = count_sim
