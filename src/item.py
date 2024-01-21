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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if 0 < len(new_name) <= 10:
            self.__name = new_name
        elif len(new_name) > 10:
            self.__name = new_name[:10]

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

    @staticmethod
    def string_to_number(value: str):
        try:
            return int(value)
        except ValueError:
            return int(float(value))

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        new_items = []

        parent_dir = os.pardir
        path_to_csv = os.path.join(parent_dir, filename)

        with open(path_to_csv, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for each_row in csv_reader:
                name = each_row['name']
                price = cls.string_to_number(each_row['price'])
                quantity = cls.string_to_number(each_row['quantity'])

                new_items.append(cls(name, price, quantity))
        Item.all = new_items
