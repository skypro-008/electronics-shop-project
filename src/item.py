import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
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
    def name(self):
        """Реализация сеттера для функции name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Реализация геттера для функции name"""
        if len(value) <= 10:
            self.__name = value
        else:
            print("Exception: Длина наименования товара превышает 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __repr__(self):
        """метод вывода"""

        class_name = self.__class__.__name__
        return f"{class_name}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @classmethod
    def instantiate_from_csv(cls):
        """Открытие файла csv"""
        cls.all = []
        with open("src\items.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name = row[0]
                price = int(row[1])
                quantity = int(row[2])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        """ Статическая функция (метод) преобразования строкового представления числа в целое число"""
        return_number = float(number)
        return int(return_number)

    def __add__(self, other):
        """Метод сложения количества"""
        if not isinstance(other, Item):
            raise Exception("Складывать можно только наследников класса Item.")
        elif not isinstance(self, Item):
            raise Exception("Складывать можно только наследников класса Item.")

        return self.quantity + other.quantity
