import csv
import os.path

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
        # Item.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name[:10]


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

    @staticmethod
    def string_to_number(num: str):
        """Статистический метод, возвращающий число из числа-строки"""
        try:
            return int(num)
        except ValueError:
            s = num.split('.')
            return int(s[0])

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        with open('../src/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                item1 = (cls(line['name'], line['price'], line['quantity']))
                cls.all.append(item1)
