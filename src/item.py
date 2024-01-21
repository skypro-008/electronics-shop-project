import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "Файл items.csv поврежден"

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
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

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
    def name(self, data_string):
        self.__name = data_string[:10]

    @classmethod
    def instantiate_from_csv(cls):
        data = "../src/items.csv"
        Item.all.clear()
        try:
            with open(data, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                if len(reader.fieldnames) != 3:
                    raise InstantiateCSVError
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None





            

