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
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise AssertionError

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price = self.price * self.quantity
        return all_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name=str):
        self.__name = name
        if len(self.__name) > 10:
            print("Длина наименования товара превышает 10 символов.")
        else:
            print("Корректное название")

    @classmethod
    def instantiate_from_csv(cls):
        item_list = []
        with open("../src/items.csv", newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = row['price']
                quantity = int(row['quantity'])
                item_list.append(Item(name, price, quantity))
            cls.all = item_list

    @staticmethod
    def string_to_number(number):
        if "." in number:
            i = number.find(".")
            return int(number[0:i])
        return int(number[0])
