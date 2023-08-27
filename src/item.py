class Item:
    pay_rate = 1.0
    all = []
    def __init__(self, article, price, quantity):
        self.price = price
        self.article = article
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate