class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price*self.quantity

    def apply_discount(self) -> None:
        discount_amount = self.price = self.price * Item.pay_rate
        return discount_amount


