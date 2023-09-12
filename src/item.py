import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.9
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
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name


    @classmethod
    def instantiate_from_csv(cls):
        """Загружает данные из файла csv"""
        cls.all = []
        with open('/home/fedor/PycharmProjects/electronics-shop-project/src/items.csv', newline='') as f:
            reader = csv.DictReader(f)
            for line in reader:
                name = line['name']
                price = float(line['price'])
                quantity = int(line['quantity'])
                Item(name, price, quantity)

    @staticmethod
    def string_to_number(digit):
        numbers = ''
        for i in range(len(digit)):
            if digit[i].isdigit():
                numbers += digit[i]
            else:
                break
        return int(numbers)
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
