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
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return int(self.quantity + other.quantity)

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
        return self.__name

    @name.setter
    def name(self, doc_string):
        if len(doc_string) > 10:
            self.__name = doc_string[:10]
        else:
            self.__name = doc_string

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open("../src/items.csv", "r", encoding="windows-1251") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Item(row['name'], float(row['price']), Item.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(string_in):
        try:
            return int(float(string_in))
        except:
            return "This is not a string"