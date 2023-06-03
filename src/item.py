import csv
from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return int(self.quantity) + int(other.quantity)
        raise ValueError("Складывать можно только экземпляры классов Item и Phone")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception("Длина названия больше 10 символов")


    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Инициализируем экземпляры класса данными из файла"""
        cls.all.clear()
        with open('/home/polexa/electronics-shop-project/src/items.csv', newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                cls(line["name"], line["price"], line["quantity"])

    @staticmethod
    def string_to_number(line):
        numb = int(float(line))
        return numb

    def calculate_total_price(self):

        return self.price * self.quantity

    def apply_discount(self):

        self.price *= self.pay_rate