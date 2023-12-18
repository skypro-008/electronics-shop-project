import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
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
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all = []
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.normpath(path))) as csv_file:
            items = csv.DictReader(csv_file)
            for item in items:
                Item(item["name"], item["price"], item["quantity"])

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __str__(self):
        return f"{self.name}, price: {self.price}, quantity: {self.quantity}"

    def __repr__(self):
        return f"{self.name}, price: {self.price}, quantity: {self.quantity}"
