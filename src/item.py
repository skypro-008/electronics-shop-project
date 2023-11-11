import csv
import os


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0

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

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise AssertionError

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

    # @classmethod
    # def instantiate_from_csv(cls, new_data=('..', 'src', 'items.csv')):
    #     with open(new_data, encoding='windows-1251') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #     try:
    #         for row in reader:
    #             name = str(row['name'])
    #             price = cls.string_to_number(row['price'])
    #             quantity = cls.string_to_number(row['quantity'])
    #             if row['name'] or row['price'] or row['quantity'] is None:
    #                 raise InstantiateCSVError
    #             item = cls(name, price, quantity)
    #             print(item)
    #     except FileNotFoundError:
    #         raise FileNotFoundError("Отсутствует файл item.csv")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, new_data=os.path.join('..', 'src', 'items.csv')):
        cls.all = []
        try:
            with open(new_data, 'r', newline='', encoding='Windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['name'] is None or row['price'] is None or row['quantity'] is None:
                        raise InstantiateCSVError("_Файл item.csv поврежден_")
                    else:
                        cls.all.append(row)
                return cls.all
        except FileNotFoundError:
            raise FileNotFoundError("_Отсутствует файл item.csv_")

    @staticmethod
    def string_to_number(num):
        return int(float(num))
