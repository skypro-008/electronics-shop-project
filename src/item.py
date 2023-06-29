import csv
import os


class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла"""
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message


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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print('Длина наименования товара превышает 10 символов')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        try:
            with open(os.path.join(os.path.dirname(__file__), 'items.csv'), newline='', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'quantity' not in row:
                        raise InstantiateCSVError

                    else:
                        name = row['name']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        cls(name, price, quantity)

        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл items.csv")

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
        self.price = self.price * self.pay_rate

    @staticmethod
    def string_to_number(number):
        number = float(number)
        return int(number)

    def __add__(self, other):
        """Сложение экземпляров класса по количеству товара в магазине"""
        if not isinstance(other, Item):
            raise ValueError
        return self.quantity + other.quantity
