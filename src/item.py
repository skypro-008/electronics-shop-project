import csv


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        discount_amount = self.price = self.price * Item.pay_rate
        return discount_amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, csv_data):
        with open(csv_data, 'r', encoding='windows-1251') as file:
            file = csv.DictReader(file)
            for info in file:
                print(info)


Item.instantiate_from_csv('../src/items.csv')
