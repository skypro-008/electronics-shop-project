import csv

from src.item import Item


class Phone(Item):
    """
    Класс для представления товара в магазине.
    """
    all_phone = []

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone, дочернего от класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        self.all_phone.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __str__(self):
        return f'{self.name}'


    @property
    def num_sim(self):
        return self.number_of_sim


    @num_sim.setter
    def num_sim(self, num):
        """Проверяет, явояется ли новое значение целым и положительным числом"""
        if isinstance(num, int) and num > 0:
            self.number_of_sim = num
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
