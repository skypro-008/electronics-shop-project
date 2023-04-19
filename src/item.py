class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []


    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.general_summ = self.price * self.quantity
        self.all = all

    def calculate_total_price(self) -> str:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return f'Общая стоимость {self.name} в магазине составляет: {self.general_summ}'

    def apply_discount(self) -> str:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return f'Цена с учетом скидки {int((1 - self.pay_rate) * 100)}% составляет {self.price}'




all1 = Item("Смартфон", 10000, 20)
all2 = Item("Ноутбук", 20000, 5)
all = [all1, all2]
