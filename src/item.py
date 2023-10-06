class Item:
    """Класс для общих данных по товару в магазине: название, цена, количество"""
    pay_rate = 0.8
    all_items = []
    def __init__(self,name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.all_items.append({"название": self.name, "цена": self.price, "количество": self.amount})

    def __str__(self):
        return f"товар {self.name}, цена за единицу {self.price}, количество {self.amount}"

    def __repr__(self):
        return f'Item(\'{self.name}\', {self.price}, {self.amount})'

    def calculate_total_price(self):
        return self.price * self.amount

    def apply_discount(self):
        return self.price * self.pay_rate