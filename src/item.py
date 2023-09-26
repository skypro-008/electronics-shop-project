import csv
import os


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Ошибка")

    def __str__(self):
        return f"{self.__name}"

    @classmethod
    def instantiate_from_csv(cls):
        csv_import = os.path.join(os.path.dirname(__file__), "items.csv")
        cls.all.clear()
        with open(csv_import, encoding='windows-1251') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

    @staticmethod
    def string_to_number(string):
        return float(string)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self) -> float:
        self.price *= self.pay_rate
        return self.price


