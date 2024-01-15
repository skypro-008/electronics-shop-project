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
        if not name:
            raise ValueError("Name cannot be empty.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара, округленная до 2 десятичных знаков.
        """

        total_price = self.price * self.quantity
        return round(total_price, 2)

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара и возвращает новую цену после применения скидки.

        :param discount: Скидка в процентах.
        """

        if not isinstance(self.pay_rate, (float, int)):
            raise ValueError("Pay rate must be a number.")

        if not 0 <= self.pay_rate <= 1:
            raise ValueError("Pay rate must be a valid percentage between 0 and 1.")

        self.price = round(self.price * self.pay_rate, 2)
