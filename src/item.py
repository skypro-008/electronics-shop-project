import csv
from pathlib import Path
from accessify import private

ROOT_DIR = Path(__file__).parent.parent
SHOP_DATA = Path.joinpath(ROOT_DIR, "items.csv")


class Item:
    """ Класс для представления товара в магазине"""

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        # self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return float(self.price * self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def all(cls):
        return cls.instances

    @property
    def product_name(self):
        """Getter для метода name"""

        return self.__name

    @product_name.setter
    def product_name(self, name):
        """Setter для метода name. Проверяем длину наименования товара """

        if len(name) >= 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса Item"""

        cls.all = []
        with open('..\src\items.csv', encoding='windows-1251') as file:
            DictReader_obj = csv.DictReader(file)
            for item in DictReader_obj:
                print(item)
                new = cls(item['name'], float(item['price']), int(item['quantity']))
                cls.all.append(new)

    @staticmethod
    def string_to_number(string):
        """Возвращает число из числа-строки"""
        return int(float(string))
