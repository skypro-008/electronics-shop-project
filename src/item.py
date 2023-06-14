import csv
import math

import os.path
class InstantiateCSVError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

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
        Item.all.append(self)
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newname):
        try:
            if len(newname) <= 15:
                self._name = newname
        except Exception:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, file="item.csv"):
        Item.all = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data = os.path.join(current_dir, file)
        try:
            with open(data, encoding="cp1251") as f:
                reader = csv.DictReader(f)
                if all(field in reader.fieldnames for field in ["name", "price", "quantity"]):
                    for row in reader:
                        cls(name=row["name"], price=float(row["price"]), quantity=int(row["quantity"]))
                else:
                    raise InstantiateCSVError(f"Файл {file} поврежден")
        except InstantiateCSVError as erorr:
            print(erorr)
        except FileNotFoundError:
            print(f"_Отсутствует файл {file}_")


    @staticmethod
    def string_to_number(num):
        number = int(math.floor(float(num.strip())))
        return number

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Нельзя складывать")
        return int(self.quantity) + int(other.quantity)
