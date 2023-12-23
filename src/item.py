import csv
from pathlib import Path


# Получаем абсолютный путь к файлу items.csv
file_path = Path(__file__).parent / 'items.csv'


class InstantiateCSVError(Exception):
    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)
class Item:
    items = []
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
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)



    def __str__(self):
        return self.name



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
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, filename=None):
        if filename is None:
            # Если filename не указан, используем относительный путь от текущей директории
            filename = Path(__file__).parent / 'items.csv'
        else:
            # Иначе используем указанный путь
            filename = Path(filename)

        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError("Файл item.csv поврежден")

                    item = cls(row['name'], float(row['price']), int(row['quantity']))
                    cls.items.append(item)
        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {filename}")

    @staticmethod
    def string_to_number(string):
        return int(string)
    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Can only add Item instances")


class KeyboardMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> None:
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

class Keyboard(Item, KeyboardMixin):
    def __init__(self, model, manufacturer, color):
        super().__init__(model, manufacturer, color)
