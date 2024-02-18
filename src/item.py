import csv
import os
from src.InstantiateCSVError import InstantiateCSVError


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

    def __repr__(self):
        """Отображает информацию об объекте класса"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Отображает информацию для пользователя"""
        return f"{self.__name}"

    def __add__(self, other):
        """Производит операцию сложения для количества товаров в магазине"""
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        """Геттер для приватного атрибута name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Проверяет длину атрибута name, если больше 10 символов - возвращает первые 10"""
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]
        return self.__name

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
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name='items.csv') -> None:
        """
        Создает экземпляры класса Item из данных в файле items.csv.
        """
        cls.all.clear()
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        try:
            with open(file_path, 'r', newline='', encoding='cp1251') as file:
                data = csv.DictReader(file)
                for row in data:
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except ValueError:
            raise InstantiateCSVError('Файл item.csv поврежден')


    @staticmethod
    def string_to_number(string):
        if string is None:
            return string
        else:
            return int(float(string))