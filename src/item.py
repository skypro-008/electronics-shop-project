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
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self.__name = new_name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

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

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.clear()
        with open(path, encoding='utf-8') as file:
            data_file = csv.DictReader(file, delimiter=',')
            for row in data_file:
                cls(row.get('name'),
                     cls.string_to_number(row.get('price')),
                     cls.string_to_number(row.get('quantity')))


    @classmethod
    def clear(cls):
        cls.all.clear()

    @staticmethod
    def string_to_number(str_num: str):
        try:
            num = int(float(str_num))
        except Exception:
            return None
        return num

    def __add__(self, other):
        if not issubclass(other.__class__, Item):
            raise TypeError('Можно складывать между собой только объекты класса Item и дочерних классов')
        return self.quantity + other.quantity
