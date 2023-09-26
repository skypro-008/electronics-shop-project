import csv
import os
import ast


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

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_cost = self.price * self.quantity
        return total_cost

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price - self.price * self.pay_rate / 100
        self.all.append(Item(self.__name, self.price, self.quantity))

    @property
    def fullname(self):
        """Возвращает полное наименование товара"""
        return self.__name

    @fullname.setter
    def fullname(self, __name):
        """Проверяет длину наименования товара"""
        if len(self.__name) < 10:
            print(self.__name)
        else:
            print(self.__name[:11])

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        dir_ = os.path.dirname(__file__)
        file_path = os.path.join(dir_, file_name)
        with open(file_path, encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"]
                price = float(row["price"])
                quantity = int(row["quantity"])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        return ast.literal_eval(number[0])
