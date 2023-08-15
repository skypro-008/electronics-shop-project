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
        self.name = name.strip()
        if not (isinstance(price, float) or isinstance(price, int)):
            raise ValueError('Цена за единицу товара должна быть только числом.')
        if price <= 0:
            raise ValueError('Цена за единицу товара может быть положительным числом!')
        self.price = price
        if not isinstance(quantity, int):
            raise ValueError('Количество товара должно быть только числом.')
        if quantity <= 0:
            raise ValueError('Количество товара может быть только положительным числом"')
        self.quantity = quantity
        self.all.append(self)

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
