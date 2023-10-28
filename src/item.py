import csv
from pathlib import Path

from src.settings import bath_dir

word_csv = []


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("No")
        return self.quantity + other.quantity

    @property
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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls) -> None:
        cls.all.clear()
        items_path = bath_dir.joinpath('items.csv')
        try:
            with open(items_path, encoding="UTF-8", errors='replace') as file:
                words = csv.DictReader(file)
                for word in words:
                    if word['name'] is None or word['price'] is None or word['quantity'] is None:
                        raise InstantiateCSVError
                    else:
                        name = word["name"]
                        price = float(word["price"])
                        quantity = int(word["quantity"])
                    cls(name, price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except InstantiateCSVError as e:
            print(e.message)



    @staticmethod
    def string_to_number(str_number: str) -> int:
        number = str_number.split('.')
        return int(number[0])
