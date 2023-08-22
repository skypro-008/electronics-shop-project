from csv import DictReader
from pathlib import Path


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

    @property
    def get_name(self):
        """Геттер для name"""

        return self.__name

    @get_name.setter
    def get_name(self, __name):
        if len(self.__name) > 10:
            self.__name = __name[0:11]

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из файла items.csv
        """
        # Переменная для csv-файла
        from_csv = Path(Path.home() / "py_project" / 'electronics-shop-project' / 'src', "items.csv")

        with open(from_csv, encoding='cp1251') as file_csv:
            reader = DictReader(file_csv)
            for unit in reader:
                name = unit['name']
                price = unit['price']
                quantity = unit['quantity']
            cls.all.append(Item(str(name), float(price), int(quantity)))

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
    def string_to_number(number_string):
        """
        Функция возвращает число из числа-строки
        """
        if '.' in number_string:
            number_float = float(number_string)
            return int(number_float)
        return int(number_string)
