import csv
import os

path = os.path.join('..', 'src', 'item.csv')  # путь к файлу


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
    def name(self, name):
        self.__name = name
        if len(self.__name) > 10:
            self.__name = self.__name[:11]

    @classmethod
    def instantiate_from_csv(cls, file):
        cls.all = []
        with open(os.path.join('..', file), encoding='windows-1251', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all = [cls((row['name']), float(row['price']), int(row['quantity'])) for row in reader]

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self, pay_rate=None) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return pay_rate

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"{__class__.__name__}('{str(self.__name)}', {str(self.price)}, {str(self.quantity)})"
