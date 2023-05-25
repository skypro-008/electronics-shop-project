from csv import DictReader
from os import path


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


    @property


    def name(self):
        return self.__name


    @name.setter


    def name(self, new_name: str) -> None:
        if len(new_name) < 11:
            self.__name = new_name
        else:
            print("Exception: Длина наименования"+\
    " товара превышает 10 символов.")


    @classmethod
    def instantiate_from_csv(cls):
        with open(path.join('..', 'src', 'items.csv'),\
        'r', encoding = 'cp1251') as csvfile:
            read = DictReader(csvfile)
            for i in read:
                cls(i['name'], i['price'], i['quantity'])


    @staticmethod


    def string_to_number(string_number: str) -> int:
        number = int(float(string_number))
        return number
