import csv
import pytest

class Item:
    pay_rate: int = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            self._name = new_name[:10]
        else:
            self._name = new_name

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename) -> None:
        items = []
        try:
            with open(filename, newline='', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if len(reader.fieldnames) != 3:
                        raise InstantiateCSVError()
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    item = cls(name, price, quantity)
                    items.append(item)
        # return items
        except FileNotFoundError:
            # print('FileNotFoundError: Отсутствует файл item.csv')
            raise FileNotFoundError('Отсутствует файл item.csv')

        except InstantiateCSVError as err:
            # print(err)
            raise InstantiateCSVError(err)



    @staticmethod
    def string_to_number(value: str) -> float:
        try:
            return float(value)
        except ValueError:
            return 0.0

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self._name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if isinstance(self.quantity, int) and isinstance(other.quantity, int):
                if self.quantity > 0 and other.quantity > 0:
                    return self.quantity + other.quantity
                else:
                    raise ValueError("Количество физических SIM-карт должно быть больше нуля")
            else:
                raise ValueError("Количество физических SIM-карт должно быть целым числом")
        return None



class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'InstantiateCSVError: Файл item.csv поврежден'

    def __str__(self):
        return self.message



