
import csv
import os

CSV_FILENAME = os.path.join("src", "items.csv")
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
        if not isinstance(name, str) or name == "":
            raise ValueError("Название товара должно быть непустой строкой")
        if not (isinstance(price, float) or isinstance(price, int)) or price <= 0:
            raise ValueError("Цена должна быть положительным числом > 0")
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Количество товара должно быть целым числом > 0")

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item({self.__name}, {self.price}, {self.quantity})"
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
        self.price *= Item.pay_rate

    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")
        return

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open(CSV_FILENAME, newline='', encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))
        return

    @staticmethod
    def string_to_number(string):
        ret, value_error = None, False
        try:
            ret = int(string)
        except ValueError:
            value_error = True
        if value_error:
            try:
                ret = float(string)
                value_error = False
            except ValueError:
                pass
        if value_error:
            raise ValueError("string_to_number: Некорректное число - строка")
        return ret