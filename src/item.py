import os
import csv

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
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.pay_rate) * self.price
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """
        Проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае,
        обрезать строку (оставить первые 10 символов)
        """
        if len(value) <= 10:
            self.__name = value
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')

    @classmethod
    def instantiate_from_csv(cls, data):
        data = f'../{data}'
        Item.all = []
        with open(data, 'r', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                lines = csvfile.readlines()
                for i in lines:
                    name, price, quantity = i.split(',')
                    print(cls(name, price, quantity))

    @staticmethod
    def string_to_number(str):
        return(int(float(str)))