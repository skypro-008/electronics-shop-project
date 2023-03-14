class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8      # атрибут кл.
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.total = None
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)  # сохоняем экземпляры класса в списке

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total = self.price * self.quantity
        return self.total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
