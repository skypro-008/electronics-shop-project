import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    max_name = 10
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > self.max_name:
            self.__name = new_name[:self.max_name]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, path):
        try:
            with open(path) as file:
                cls.all.clear()
                for row in csv.DictReader(file):
                    cls.all.append(
                        Item(
                            row["name"],
                            row["price"],
                            row["quantity"],
                        )
                    )
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except Exception:
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name, self.price, self.quantity}'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise ValueError('ошибка')
