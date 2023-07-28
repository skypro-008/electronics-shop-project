from csv import DictReader

from settings import PATH_ITEMS_CSV


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    items_csv_path = PATH_ITEMS_CSV

    def __init__(self, name, price, quantity):
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
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) >= 10:
            raise ValueError('More than 10 letters in the name')
        else:
            self.__name = new_name
    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open(cls.items_csv_path, 'r', encoding='windows-1251') as csv:
            data = DictReader(csv)
            for item in data:
                cls(
                    name=item['name'],
                    price=cls.string_to_number(item['price']),
                    quantity=cls.string_to_number(item['quantity'])
                )

    @staticmethod
    def string_to_number(decimal_string):
        return int(float(decimal_string))


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
