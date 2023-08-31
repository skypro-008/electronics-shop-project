from csv import DictReader
import csv
import os

PATH_ABSOLUTE = os.path.join(os.path.dirname(__file__), "items.csv")


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
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

        # self.all.append(Item)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname: str):
        if len(newname) > 10:
            self.__name = newname[:10]
        else:
            self.__name = newname

    @classmethod
    def instantiate_from_csv(cls,
                             path_from_csv=PATH_ABSOLUTE) -> None:
        """
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        with open(path_from_csv, newline="", encoding="cp1251") as csvfile:
            reader = DictReader(csvfile, fieldnames=["name", "price", "quantity"], dialect=csv.unix_dialect)
            count = 0
            for row in reader:
                if count == 0:
                    pass
                else:
                    cls.all.append(Item(row["name"], float(row["price"]), int(row["quantity"])))
                count += 1

    @staticmethod
    def string_to_number(str_number: str):
        """
        Возвращает число из числа-строки
        """
        return int(float(str_number))

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
