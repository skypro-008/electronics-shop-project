import csv
import os

from src.phone import Phone


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            total_quantity = self.quantity + other.quantity
            return total_quantity
        elif isinstance(other, Phone):
            total_quantatity = self.quantity +other.quantity
            return total_quantatity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError("Длина наименования превышает 10 символов")



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> list:
        cls.all = []
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(ROOT_DIR, 'items.csv'), newline='') as file:
            rows = csv.DictReader(file)
            for row in rows:
                name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                item = cls(name, price, quantity)
                cls.all.append(item)
        # проверяем уникальность имен и оставляем только уникальные комбинации имя: ключ и преобразует экземпляры классов(ключи) в список
        cls.all = list({item.name: item for item in cls.all}.values())
        return cls.all



    @staticmethod
    def string_to_number(string: str) -> int:
        if "." in string:
            number = int(float(string))

        else:
            number = int(string)
        return number


