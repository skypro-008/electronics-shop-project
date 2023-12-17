import csv
import os

# file_path = os.path.join('..', 'src', 'items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_path = os.path.join('..', 'src', 'items.csv')

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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        if len(self.__name) > 10:
            self.__name = self.__name[:11]

    @classmethod
    def instantiate_from_csv(cls, file_name=None):
        cls.file_name = file_name
        cls.all.clear()
        if not file_name:
            raise FileNotFoundError(f"Отсутствует файл")

        try:
            with open(file_name, encoding='windows-1251', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError("Файл item.csv поврежден.")
                    name = row["name"]
                    price = float(row["price"])
                    quantity = cls.string_to_number(row["quantity"])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self, pay_rate=None) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return pay_rate

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"{__class__.__name__}('{str(self.__name)}', {str(self.price)}, {str(self.quantity)})"

    def __add__(self, other):
        """Метод сложения количества телефонов класса Item и его наследников"""
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только экземпляры Item и Phone')
        return self.quantity + other.quantity


class InstantiateCSVError(Exception):

    def __init__(self, message):
        self.message = message  # Файл item.csv поврежден

    def __str__(self):
        return f'{self.message}'
