class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(str(self))
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

    def calculate_total_price(self) -> float:
        total = self.price * self.quantity
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        #Item.all.append(total)
        return total

    def apply_discount(self) -> None:
        self.price *= Item.pay_rate
        return self.price

    """
    Применяет установленную скидку для конкретного товара.       
    """
