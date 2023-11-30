import csv
import math
from typing import Any


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
        self.all.append(self)

    @property
    def name(self) -> str:
        """
        Возвращает наименование товара.
        """
        return self.__name

    @name.setter
    def name(self, quantity: str) -> None:
        """
        Устанавливает наименование товара.
        """
        if len(quantity) > 10:
            self.__name = quantity[:10]
        else:
            self.__name = quantity

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
        self.price = self.price * self.pay_rate

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса
        (для разработчиков)
        """
        return (
            f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"
        )

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса
        (для пользователей)
        """
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, file_path: Any) -> None:
        """
        Класс-метод, инициализирующий экземпляры класса Item
        """
        cls.all.clear()
        with open(file_path, encoding="windows-1251") as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                name = row["name"]
                price = float(row["price"])
                quantity = cls.string_to_number(row["quantity"])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(math.floor(float((string.replace(",", ".")))))
