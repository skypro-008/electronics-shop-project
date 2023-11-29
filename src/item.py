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

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            Exception('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self, pay_rate) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        """
        создает список экземпляров класса Item
        """
        cls.all.clear()
        cls.all = []
        with open('../src/items.csv', 'r', encoding="cp1251", newline='') as csv_file:
            read_file = csv.DictReader(csv_file)
            for i in read_file:
                name = i["name"]
                price = float(i["price"])
                quantity = int(i["quantity"])
                item = cls(name, price, quantity)
                cls.all.append(item)

    @staticmethod
    def string_to_number(num):
        """
        возвращающий число из числа-строки
        """
        number = int(float(num))
        return number
