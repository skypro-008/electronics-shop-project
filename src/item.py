
import csv
import os

#items_csv = os.path.join("items.csv")
items_csv = r'D:\PycharmProjects\pythonProject\electronics-shop-project\src\items.csv'

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


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"


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
        """
        Выводит имя объекта класса Item
        """
        return self.__name


    @name.setter
    def name(self, name):
        """
        Присваивает новое имя объекту класса Item, длинной не более 10 символов
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name


    @classmethod
    def instantiate_from_csv(cls):
        """
        Создает объекты класса Item на основе файла "items.csv"
        """
        with open(items_csv, encoding="windows-1251") as csvfile:
            file = csv.DictReader(csvfile)
            for line in file:
                name, price, quantity = line["name"], float(line["price"]), cls.string_to_number(line["quantity"])
                cls(name, price, quantity)


    @staticmethod
    def string_to_number(string):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(string))

