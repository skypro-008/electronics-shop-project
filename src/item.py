import csv

import pytest


class InstantiateCSVError(Exception):
    def __init__(self):
        self.massage = "Файл item.csv поврежден"

    def __str__(self):
        return self.massage


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
        return f"{self.__class__.__name__}('{self.__name}', {int(self.price)}, {int(self.quantity)})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[0:10]
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        price_all = self.price * self.quantity
        return price_all

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name="..\src\items.csv"):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """

        try:
            with open(file_name, newline="") as csfile:
                reader = csv.DictReader(csfile)
                for row in reader:
                    try:
                        list_item = cls(row["name"], row["price"], row["quantity"])
                        if row["quantity"] == None or row["price"] == None or row["name"] == None:
                            raise InstantiateCSVError
                    except InstantiateCSVError as ex:
                        print(ex)
                        raise
                    cls.all.append(list_item)
        except FileNotFoundError:
            print(f"Отсутствует файл {file_name}")
            raise

    @staticmethod
    def string_to_number(str_number):
        """
        статический метод, возвращающий число из числа-строки
        """
        int_number = int(float(str_number))
        return int_number
