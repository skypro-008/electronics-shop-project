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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

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
        self.price *= self.pay_rate

    @property
    def fullname(self):
        """Возвращает полное наименование товара"""
        return self.__name

    @fullname.setter
    def fullname(self, new_name):
        """Проверяет длину наименования товара"""
        if len(new_name) < 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

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
        return int(float(number))
