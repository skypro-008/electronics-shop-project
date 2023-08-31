import csv

class InstantiateCSVError(Exception):

    def __init__(self):
        self.message = 'Файл items.csv поврежден'

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
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[:10]
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, path):
        try:
            with open(path, encoding='CP1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError()
                    cls.all.append(cls(row["name"], row["price"], row["quantity"]))
        except:
            print('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(str):
        str_to_num = str.split('.')
        return int(str_to_num[0])

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Нельзя сложить экземпляры классов отличные от Item или Phone')
        return self.quantity + other.quantity