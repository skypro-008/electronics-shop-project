import csv

from src.error import InstantiateCSVError


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

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            Exception('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self, pay_rate) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, file='../src/items.csv'):
        """
        создает список экземпляров класса Item
        """
        try:
            cls.all.clear()
            cls.all = []
            with open(file, 'r', encoding="cp1251", newline='') as csv_file:
                read_file = csv.DictReader(csv_file)
                for i in read_file:
                    if i['name'] is None or i['price'] is None or i['quantity'] is None:
                        raise InstantiateCSVError("Файл items.csv поврежден")
                    else:
                        name = i["name"]
                        price = float(i["price"])
                        quantity = int(i["quantity"])
                        item = cls(name, price, quantity)
                        cls.all.append(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(num):
        """
        возвращающий число из числа-строки
        """
        number = int(float(num))
        return number

    def __add__(self, other):
        """
        складывает quantity экземпляров класса Item u Phone
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
