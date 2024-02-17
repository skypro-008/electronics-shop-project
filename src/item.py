import csv
from config import root_csv

class Item():
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

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 10:
            self.__name = name[0:10]
        else:
            self.__name = name

    name = property(get_name, set_name)

    @classmethod
    def instantiate_from_csv(cls, csvfile):
        """
        класс-метод, инициализирует экземпляры класса Item
        """
        cls.all = []
        count = 0
        with open(csvfile, encoding='windows-1251') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=",")
            for row in file_reader:
                name, price, quantity = str(row['name']), float(row['price']), int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(str_number):
        """
         статический метод, возвращающий число из числа-строки
        """
        number = float(str_number)
        return int(number)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

