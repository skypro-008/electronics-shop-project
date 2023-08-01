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
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
        if len(new_name) > 10:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """Метод класса для создания экземпляров из файла"""
        Item.all = []
        with open('items.csv') as f:
            data = list(csv.reader(f))
        for item in data[1:]:
            name = item[0]
            price = float(item[1])
            quantity = int(item[2])
            cls(name, price, quantity)

    @staticmethod
    def string_to_number(string_number):
        return int(float(string_number))
