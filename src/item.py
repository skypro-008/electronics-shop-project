import csv
import math


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
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        """ Возвращает наименование товара. """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """ Устанавливает наименование товара. """
        if len(name) > 10:
            self.__name = name[:10]
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
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        """инициализирует экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()
        with open(filename, 'r', encoding="windows-1251") as file:
            reader = csv.DictReader(file, delimiter=',')
            for line in reader:
                name = line['name']
                price = Item.string_to_number(line['price'])
                quantity = int(line['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string: str) -> float:
        """Преобразование строки в число"""
        return int(math.floor(float((string.replace(',', '.')))))


def __repr__(self) -> str:
    return f"Item('{self.name}', {self.price}, {self.quantity})"


def __str__(self) -> str:
    return f"{self.name}"


def __add__(self, other):
    if isinstance(other, Item):
        return self.quantity + other.quantity
    else:
        raise TypeError("Unsupported operation")
