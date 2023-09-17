import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__()
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
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        if len(name_str) > 10:
            self.__name = name_str[0:10]
        else:
            self.__name = name_str


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
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                item = cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(number):
        numbers = number.split(".")
        return int(number[0])
