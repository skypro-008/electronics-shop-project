class Item:
    pay_rate = 0.5
    all = []

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        return self.price * self.quantity
