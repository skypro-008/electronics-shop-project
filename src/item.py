from csv import DictReader
from pathlib import Path
from src.errors import InstantiateCSVError


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
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        if len(self.__name) > 10:
            self.__name = name[:10]
            return name[:10]
        else:
            return name

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all.clear()
        work_dir = Path.cwd()
        path = Path(work_dir.parent, path)
        try:
            with open(path, encoding='Windows-1251') as csv:
                reader = DictReader(csv)
                for row in reader:
                    if len(row.keys()) <= 4 or any(value is None or value == '' for value in row.values()):
                        raise InstantiateCSVError()
                    cls(name=row['name'],
                        price=row['price'],
                        quantity=row['quantity']
                        )
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {str(path)}')

    @staticmethod
    def string_to_number(string: str) -> int:
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(type(other), self.__class__):
            return self.quantity + other.quantity
        return NotImplemented



