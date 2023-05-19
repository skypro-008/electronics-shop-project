import csv
import os

# Создаем константу с путем к файлу
PATH = os.path.abspath('../src')
PATH_TO_ITEMS = os.path.join(PATH, 'items.csv')

class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self) -> float:
        """Возвращает общую стоимость конкретного товара"""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет скидку для товара"""
        self.price *= self.pay_rate

    @property
    def name(self):
        """Возвращает наименование товара"""
        return self.__name

    @name.setter
    def name(self, __name):
        """Проверяет наименование на количество символов"""
        if len(__name) < 10:
            self.__name = __name
        else:
            print('Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализирует экземпляры из файла csv"""
        with open(PATH_TO_ITEMS, encoding='Windows-1251') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))
                Item.all.append(cls(row['name'], int(row['price']), int(row['quantity'])))

    @staticmethod
    def string_to_number(value):
        """Возвращает число из числа-строки"""
        if '.' not in value:
            return int(value)
        else:
            return int(float(value))
