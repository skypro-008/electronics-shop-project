class Item:

    pay_rate = 0.85 #для хранения уровня цен с учетом скидки
    all = [] #для хранения созданных экземпляров класса

    def __init__(self,name:str,price:int,quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        return self.price * self.quantity
