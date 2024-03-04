import csv
import os

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8

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
        return f"{self.__name}"

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self, pay_rate) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price *  pay_rate

    @name.setter
    def name(self, value):
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls, file_name):


        cls.all.clear()
        with open(file_name, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                name = item['name']
                price = cls.string_to_number(item['price'])
                quantity = int(item['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    #def __add__(self, other):
    #    """
    #    Метод сложения количества товаров двух классов
    #     """

    #    if not isinstance(other, Item):
    #        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
    #    else:
    #        return self.quantity + other.quantity
