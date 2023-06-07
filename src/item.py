import csv
import math


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
        """
        :return: Возвращает представление объекта для разработки
        """
        return f"Item('{self.name}',{self.price},{self.quantity})"

    def __str__(self):
        """
        :return: Возвращает представление объекта для пользователя
        """
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return None

    @property
    def name(self):
        """
        :return: Возвращает название экземпляра класса
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Устанавливает название в экземпляр класса
        """
        try:
            if len(name) <= 10:
                self.__name = name
            else:
                raise Exception(f"Длина наименования {name} товара превышает 10 символов.")
        except Exception as ex:
            print(ex)

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

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса `Item`
        """
        cls.all = []
        with open('../src/items.csv', 'r', newline='') as csvfile:

            reader = csv.DictReader(csvfile)
            for row in reader:

                Item(row["name"], row["price"], row["quantity"])

    @staticmethod
    def string_to_number(num):
        """
        Возвращает число из числа-строки
        """
        return math.floor(float(num))
