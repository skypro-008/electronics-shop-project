class Item:
    """
    Класс представления товара
    """
    pay_rate = 1
    all = []

    def __init__(self, title: str, price: float, total_items: int):
        self.title = title
        self.price = price
        self.total_items = total_items
        Item.all.append(self)

    def calculate_total_price(self):
        """
        Метод возвращает общее кол-во товара в магазине
        """
        total_price = self.price * self.total_items
        if self.total_items == 0:
            return f"Товар закончился"
        return total_price

    def apply_discount(self) -> float:
        """
        Метод возвращает цену в зависимости от коэ-та скидки
        """
        self.price *= Item.pay_rate
        return self.price
