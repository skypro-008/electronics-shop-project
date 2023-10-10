class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, amount):
        """Класс данных по товару в магазине: название, цена, количество"""
        self.name = name
        self.price = price
        self.amount = amount
        self.all.append(self)
        pass

    def calculate_total_price(self):
        """Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.price * self.amount
        pass

    def apply_discount(self):
        """Применяет установленную скидку для конкретного товара."""
        self.price *= self.pay_rate
        pass
