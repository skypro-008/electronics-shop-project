import csv
import os.path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла src/items.csv"""
        with open(file_name, encoding='windows-1251') as csvfile:
            cls.all.clear()
            reader = csv.DictReader(csvfile)
            for attribute in reader:
                cls(attribute['name'], float(attribute['price']), int(attribute['quantity']))

    @staticmethod
    def string_to_number(string):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(string))

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
        """Возвращает имя"""
        return self.__name

    @name.setter
    def name(self, name):
        """Проверяет, что длина наименования товара не больше 10 симвовов. В противном случае, обрезает строку, оставив первые 10 символов)"""
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]


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