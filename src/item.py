import csv
import os.path
import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name_: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param __name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name_
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_: str):
        """
        Присваивает экземпляру атрибут __name: str ,
        после проверки: длина строки должна быть не более 10,
        если входящая строка больше 10, то обрезается до 10  символов.
        """
        if len(name_) <= 10:
            self.__name = name_
        else:
            self.__name = name_[0:10]

    @classmethod
    def instantiate_from_csv(cls, file_name):
        n_dir, n_file = file_name.split('/')
        file_name = os.path.join('..', n_dir, n_file)
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                name_ = line['name']
                price = float(line['price'])
                quantity = Item.string_to_number(line['quantity'])
                x = cls(name_, price, quantity)
                x.name = name_


    @staticmethod
    def string_to_number(str_):
        '''статический метод, возвращающий число из числа-строки'''

        l = str_.split('.')
        if not l[0].isdigit():
            number = 0
        else:
            number = int(l[0])
        return number

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*self.pay_rate

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError(f'{other} не принадлежит классу Item и его подклассам')
        return self.quantity + other.quantity


