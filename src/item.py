class Item:
    """
    Класс для представления товара в магазине.
    """
    instances: int
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount_level = 1.0
        self.instances = 0

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.discount_level * self.instances

    def apply_discount(self, discount_level) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.discount_level = discount_level

    def get_total_price(self):
        return self.price * self.discount_level * self.instances

    def add_instance(self):
        self.instances += 1