from settings import ITEM_CSV_PATH
from csv import DictReader
from src.exeption import InstantiateCSVError
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    items_csv = ITEM_CSV_PATH

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
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]


    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f'{self.__name}'


    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            print('Складывать можно только количество на складе')


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

    @classmethod
    def instantiate_from_csv(cls, filename="../src/items.csv"):
        cls.all = []
        if os.path.exists(filename) == False:
            raise FileNotFoundError('Отсутсвует файл items.csv')

        else:
            with open(cls.items_csv, 'r', encoding='windows-1251') as csv:
                data = DictReader(csv)
                try:
                    for item in data:
                        cls(
                            name=item['name'],
                            price=cls.string_to_number(item['price']),
                            quantity=cls.string_to_number(item['quantity'])
                        )
                except KeyError:
                    raise InstantiateCSVError('Файл items.csv поврежден')



    @staticmethod
    def string_to_number(decimal_string):
        return int(float(decimal_string))
