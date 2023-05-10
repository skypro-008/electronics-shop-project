import csv
import os
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity

        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

    """Phone` и `Item`  метод сложения по количеству товара в магазине"""
    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        total = self.price * self.quantity
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return total

    def apply_discount(self) -> None:
        self.price *= Item.pay_rate
        return self.price

    """
    Применяет установленную скидку для конкретного товара.       
    """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name
        else:
            raise Exception('Ошибка: в наименовании товара больше 10 символов')

    @classmethod
    def instantiate_from_csv(cls) -> None:
        itemscsv = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'src', 'items.csv')
        with open(itemscsv, 'r', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = cls(row.get('name'), float(row.get('price')), int(row.get('quantity')))
                cls.all.append(item)


    @staticmethod
    def string_to_number(num):
        return float(num).__int__()

   

