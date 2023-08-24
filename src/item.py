class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    keep = True

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self._price = price
        self._quantity = quantity

        if Item.keep:
            Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self._price * self._quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self._price *= self.pay_rate # мой ООП Мир покинул чат...

    @property
    def price(self) -> float:
        return self._price
