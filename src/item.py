import csv
from ctypes import Union


class Item:
    """
    Класс для представления товара в магазине.
    """
    CSV = None
    pay_rate = 1.0
    all = []

    def __init__(self, _name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param _name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = _name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Геттер для наименования товара.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Сеттер для наименования товара.

        :param new_name: Новое наименование товара.
        """
        try:
            if len(new_name) <= 10:
                self._name = new_name
            else:
                raise ValueError("Длина наименования товара превышает 10 символов.")
        except ValueError as e:
            print(e)

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Создание экземпляров класса `Item` на основе данных из файла _src/items.csv_.
        """
        cls.all.clear()
        try:
            with open('/home/polexa/electronics-shop-project/src/items.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print('Файл не найден')


import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    CSV = None
    pay_rate = 1.0
    all = []

    def __init__(self, _name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param _name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = _name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Геттер для наименования товара.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Сеттер для наименования товара.

        :param new_name: Новое наименование товара.
        """
        try:
            if len(new_name) <= 10:
                self._name = new_name
            else:
                raise ValueError("Длина наименования товара превышает 10 символов.")
        except ValueError as e:
            print(e)

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Создание экземпляров класса `Item` на основе данных из файла _src/items.csv_.
        """
        cls.all.clear()
        try:
            with open('/home/polexa/electronics-shop-project/src/items.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print('Файл не найден')

    @staticmethod
    def string_to_number(line):
        numb = int(float(line))
        return numb

    def calculate_total_price(self):

        return self.price * self.quantity

    def apply_discount(self):

        self.price *= self.pay_rate
