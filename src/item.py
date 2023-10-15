import csv
import os


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
        self.total_ = 0

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_ = self.price * self.quantity
        return self.total_

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    # @classmethod
    # def instantiate_from_csv(cls, new_data):
    #     with open(new_data, 'r', newline='', encoding='Windows-1251') as csvfile:
    #         fieldnames = ['name', 'price', 'quantity']
    #         reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    #         for row in reader:
    #             name = row['name']
    #             price = row['price']
    #             quantity = row['quantity']


    @staticmethod
    def string_to_number(num):
        return int(float(num))




