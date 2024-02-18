import csv
import os

# file_proba ="../src/item.csv" # тестируем правильный файла
# file_proba ="../src/item1.csv" # тестируем отсутствие файла
# file_proba ="../src/item2.csv" # тестируем повреждение файла


class InstantiateCSVError(Exception):
    """
    Класс проверки на повреждение файла данных

    """
    def __init__(self, *args):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return f'{self.message}'


class Item:

    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
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

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    @property
    def name(self):
        """
        Геттер
        """
        return self.__name

    @name.setter
    def name(self, value: str):
        """
        Сеттер с проверкой длины имени
        """
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, file_proba):
        cls.file_proba = file_proba
        """
        Формирование экземпляров класса Item из внешнего файла
        """
        if not os.path.isfile(cls.file_proba):
            raise FileNotFoundError("Отсутствует файл item.csv")
        else:
            cls.all.clear()
            with open(cls.file_proba, 'r', newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError
                    else:
                        name = row['name']
                        price = row['price']
                        quantity = row['quantity']
                        cls(name, price, quantity)
        return cls

    @staticmethod
    def string_to_number(value):
        """
        Преобразование строки в число
        """
        value_int = int(float(value))
        return value_int

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        """
        Реализация возможности сложения экземпляров классов
        (сложение по количеству товара в магазине)
        """
        if isinstance(other, self.__class__):
            return int(self.quantity) + int(other.quantity)
