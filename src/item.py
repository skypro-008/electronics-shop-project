import csv
from pathlib import Path
from typing import List


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all: List = []

    @staticmethod
    def string_to_number(string_number: str) -> int:
        """
                Статметод переводит число заданное строкой в целое число
                :param string_number - строка, содержащая число

                :return: целое число.
                """
        return int(float(string_number))

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
        self.all = self.all.append(self)

    @property
    def name(self) -> str:
        """ Геттер для приватного атрибута name"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """ Сеттер для приватного атрибута name
        Проверяет длину имени name, если больше 10 символов обрезает строку"""
        if len(name) <= 10:
            self.__name = name
        else:
            print('Exception: Длина наименования товара превышает 10 символов.')
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, relative_path: str) -> None:
        """ Классовый метод
        Инициализирует экземпляры класса `Item` данными из файла _src/items.csv
        :param relative_path - относительный путь к файлу csv
                """
        cls.all = []
        with open(Path.cwd().parents[0] / relative_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                cls(name, float(price), int(quantity))

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
