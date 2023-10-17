import csv

from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        """
        выводит информацию об объекте для backend
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        выводит информацию об объекте для пользователя
        """
        return f'{self.name}'

    def __add__(self, other):
        """
        складывает количество товра в из класса Item с твоаром
        из другого класса
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        """
        проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае, обрезаут строку, оставляя первые 10 символов
        """
        if int(len(value)) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @staticmethod
    def string_to_number(string: str):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(string))

    @classmethod
    def instantiate_from_csv(cls):
        """
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        cls.all.clear()
        file = Path(__file__).parent.joinpath('items.csv')
        with open(file, 'r', encoding='windows-1251') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row["quantity"])
                cls(row["name"], price, quantity)
        return cls.all

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * float(self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
print(Item.all)
