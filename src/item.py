import csv
import json


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.general_summ = self.price * self.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print('Exception: Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> str:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return f'Общая стоимость {self.__name} в магазине составляет: {self.general_summ}'

    def apply_discount(self) -> str:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return f'Цена с учетом скидки {int((1 - self.pay_rate) * 100)}% составляет {self.price}'

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """

        with open('D:\SKY_PRO\Home_work\Home_work_13_1_Electronics-Store\src\items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                cls.all.append(cls(row['name'], int(row['price']), int(row['quantity'])))
        return len(cls.all)
        print(cls.all)

    @staticmethod
    def string_to_number(number):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(number))

# print(Item.all[1])
