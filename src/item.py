class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price * self.pay_rate
        self.quantity = quantity
        Item.all.append(self)
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

#item1 = Item('Смартфон', 10000, 20)
#item2 = Item('Ноутбук', 20000, 5)
# print(item1.calculate_total_price())
#print(item2.calculate_total_price())
# Item.pay_rate = 0.8
# print(item1.apply_discount())
#print(item2.price)