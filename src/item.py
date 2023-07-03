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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(self.__name) > 10:
            raise ValueError('Длинна товара превышает 10 символов')
        else:
            self.__name = name[:10]



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):

        with open('C:/Users/Ruslan/PycharmProjects/electronics-shop-project/src/items.csv ', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name,price,quantity)
            cls.all.append(item)
            cls.all.pop()


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        return int(self.quantity) + int(other.quantity)

    @staticmethod
    def string_to_number(stroka):
        num = float(stroka)
        int_num = int(num)
        return int_num