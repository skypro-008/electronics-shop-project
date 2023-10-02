import csv
import math
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self._name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            return ValueError
        return self.quantity + other.quantity
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        """проверка длины"""

        self._name = name[:10]

    @classmethod
    def string_to_number(cls, string):
        pass


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', encoding='cp1251') as csvfile:
            read = csv.DictReader(csvfile)
            for x in read:
               name = x["name"]
               price = x["price"]
               quantity = x["quantity"]
               item = cls(name, price, quantity)
               Item.all.append(item)
            return Item.all


    @staticmethod
    def string_to_number(line):
        x = float(line)
        return int(x)