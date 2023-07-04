import csv
import math
import os

path_to_file = os.path.join(os.path.dirname(__file__), 'items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_cost = self.quantity*self.price
        return total_cost

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """Читает файл со списком товаров, преобразует
        в объекты класса Item и записывает их в атрибут all"""
        # Очистка списка all перед записью
        cls.all.clear()
        with open(path_to_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))
                cls.all.append(item)

    @staticmethod
    def string_to_number(number_str):
        return math.floor(float(number_str))
