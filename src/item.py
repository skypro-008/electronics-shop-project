import csv
import os
from pathlib import Path
from src.errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.join(os.path.dirname(__file__), "items.csv")  # путь к csv-файлу

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        if not os.path.exists(cls.CSV_PATH):
            raise FileNotFoundError(f"Отсутствует файл {Path(cls.CSV_PATH).name}")

        try:
            with open(cls.CSV_PATH) as file:
                reader = csv.DictReader(file)
                cls.all.clear()
                for line in reader:
                    item = cls(line['name'], float(line['price']), int(line['quantity']))
        except (KeyError, TypeError):
            raise InstantiateCSVError(f"Файл {Path(cls.CSV_PATH).name} поврежден")

    @staticmethod
    def string_to_number(string):
        """Cтатический метод, возвращающий число из числа-строки"""
        return int(float(string))

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.quantity = quantity
        self.price = price
        self.__name = name
        self.all.append(self)

    def __repr__(self):
        """Отображение информации об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Отображение информации об объекте класса для пользователей"""
        return f"{self.__name}"

    def __add__(self, other):
        """Складываем только экземпляры класса Item и его дочерних классов"""
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self):
        """Возвращает имя"""
        return self.__name

    @name.setter
    def name(self, name):
        """Обрезает имя, если оно больше 10 символов"""
        if len(name) > 10:
            self.__name = name[0:10]
        else:
            self.__name = name

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
