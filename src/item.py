from accessify import private, protected
import csv
import os

PATH_TO_ITEMS_CSV = os.path.join("..", "src", "items.csv")


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
        Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {str(self.quantity)})'

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return round(self.price * self.quantity, 1)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_string):
        if len(name_string) > 10:
            self.__name = name_string[:10]
        else:
            self.__name = name_string

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        with open(PATH_TO_ITEMS_CSV, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string_num):
        return int(float(string_num))
