import csv


class Item:
    path = 'src/items.csv'
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path) as file:
            for row in csv.DictReader(file):
                cls.all.append(
                    Item(
                        row["name"],
                        row["price"],
                        row["quantity"],
                    )
                )

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name, self.price, self.quantity}'

    def __str__(self):
        return self.name




