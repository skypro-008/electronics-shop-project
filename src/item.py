import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "Файл item.csv поврежден"


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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты классов Item и Phone.")
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data_string: str):
        name = data_string
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.csv'):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) != 3 or row['name'] is None or row['price'] is None or row['quantity'] is None:
                        raise InstantiateCSVError
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
            raise
        except InstantiateCSVError as err:
            print(err.message)
            raise

    @staticmethod
    def string_to_number(number: str):
        return int(float(number))

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
