import csv
import os


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
        """Возвращает информацию о классе по шаблону <Item(name, price, quantity)>"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает название товара указанного класса"""
        return self.__name

    def __add__(self, other):
        """Складывает экземпляры классов `Phone` и `Item` по количеству товара в магазине"""
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Phone и Item.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

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
        """Оставляет от наименования товара первые 10 букв"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all = []
        src_path = os.path.dirname(__file__)
        src_filename = "items.csv"
        file_path = os.path.join(src_path, src_filename)

        with open(file_path, encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                cls(item['name'], float(item['price']), int(item['quantity']))

    @staticmethod
    def string_to_number(string):
        """Статический метод, возвращающий число из числа-строки"""
        return int(float(string))
