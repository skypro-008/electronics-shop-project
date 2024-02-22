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
        pass

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        pass

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        pass

import csv

class Item:
    # Атрибут класса для хранения скидки
    pay_rate = 1
    all = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.total_price = price * quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @staticmethod
    def string_to_number(value):
        return int(value) if value.isdigit() else float(value)

    @classmethod
    def instantiate_from_csv(cls):
        with open('src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))