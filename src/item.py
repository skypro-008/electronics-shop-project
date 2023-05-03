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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open("../src/items.csv") as f:
            data = csv.DictReader(f)
            for k in data:
                obj = (cls(name=k["name"], price=k["price"], quantity=k["quantity"]))






    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        if len(name) <= 10:
            self.__name = name
        raise Exception("Длина наименования товара превышает 10 символов")
    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*self.pay_rate


    @staticmethod
    def string_to_number(str_num):
        try:
            return int(float(str_num))
        except ValueError:
            print("Это не число")