import csv

class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Файл items.csv поврежден'

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):

        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

       """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @property
    def name(self) -> str:
        return self.__name


    @name.setter
    def name(self, amount: str) -> None:
        if len(amount) <= 10:
            self.__name = amount
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")


    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open('src/items.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError()
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    item = cls(name, price, quantity)
                    cls.all.append(item)
                return cls.all
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")


    @staticmethod
    def string_to_number(value):
        return float(value)