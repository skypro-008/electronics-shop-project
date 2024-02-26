import csv


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

    def __repr__(self):
        """Использование метода repr для вывода экземпляров класса"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Создание метода str для вывода экземпляров класса"""
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """Функция проверяет длину наименования товара, чтобы было не более 10 символов"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, items='../src/items.csv'):
        """Добавление экземпляра класса из csv файла"""
        cls.all = []
        with open(items, encoding="windows-1251") as csv_file:
            read = csv.DictReader(csv_file)
            rows = list(read)
            for row in rows:
                Item(str(row['name']), float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(str_number):
        """Возвращает число из числа-строки"""
        number = float(str_number)
        return int(number)

    def __add__(self, other):
        """
        Реализация возможности сложения экземпляров класса `Phone` и `Item`
        (сложение по количеству товара в магазине)
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return ValueError("Складывать можно только объекты классов с родительским классом Item")
