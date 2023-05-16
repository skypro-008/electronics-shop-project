class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)


    def calculate_total_price(self, price) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.price = price
        total_price = sum(price)
        return total_price

    def apply_discount(self, total_price=None, pay_rate=None) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return total_price * pay_rate
    
