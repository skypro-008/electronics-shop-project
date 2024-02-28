import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

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
        self.price *= self.pay_rate


    @property
    def name(self):
        return self.__name

    @name.setter
    #проверяет, что длина наименования товара не больше 10 симвовов.
    # В противном случае, обрезает строку (оставляет первые 10 символов)

    def name(self, value):
        if len(value) <= 10:
            self.__name = value
            print(value)
        else:
            self.__name = value[:10]
            print(value[:10])


    @classmethod
    #инициализирует экземпляры класса Item данными из файла src/items.csv

    def instantiate_from_csv(cls, path='../src/items.csv'):

        if not os.path.exists(path):
            raise FileNotFoundError('Отсутствует файл item.csv.')

        cls.all.clear()
        with open(path, encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "name" not in row or "price" not in row or "quantity" not in row:
                    raise InstantiateCSVError
                else:
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    cls(name, price, quantity)



    @staticmethod
    #возвращаает число из числа-строки

    def string_to_number(value):
        return int(float(value))


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Складывать можно только объекты класса с родительским классом Item")


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Файл item.csv поврежден'

    def __str__(self):
        return self.message

class FileNotFoundError(Exception):
    pass




