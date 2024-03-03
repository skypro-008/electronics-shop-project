import csv
import os.path

from src.instantiatecsv import InstantiateCSVError


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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, string_name):
        if len(string_name) > 10:
            self.__name = string_name[0:10]
        else:
            self.__name = string_name

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
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name):
        if not os.path.exists(file_name):
            raise FileNotFoundError("_Отсутствует файл item.csv_")
        else:
            cls.all.clear()
            with open(file_name, newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError('_Файл item.csv поврежден_')
                    else:
                        name = row["name"]
                        price = row["price"]
                        quantity = cls.string_to_number(row["quantity"])
                        cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя складывать с другими классами, кроме Phone")
