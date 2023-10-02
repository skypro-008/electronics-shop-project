import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "_Файл item.csv поврежден_"

    def __str__(self):
        return self.message


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, " \
               f"{self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError
        return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.csv') -> None:
        Item.all = []
        try:
            with open(filename, newline='',
                      encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                        name = str(row['name'])
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                except KeyError:
                    raise InstantiateCSVError
                else:
                    cls(name, price, quantity)

        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv_')
        except InstantiateCSVError as m:
            print(f"InstantiateCSVError: {m.message}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name
        if len(name) >= 10:
            name = name[:10]
            self.__name = name

    @staticmethod
    def string_to_number(data: str) -> int:
        if len(data) > 1:
            return int(data.split('.')[0])
        return int(data)

    def calculate_total_price(self) -> float:
        return self.quantity * self.price

    def apply_discount(self) -> None:
        self.price *= self.pay_rate