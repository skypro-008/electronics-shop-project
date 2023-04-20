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
        self.all.append(self)

    # @property
    # def name(self):
    #     return self.name

    # @name.setter
    # def name(self, name):
    #     leen = len(name)
    #     if leen <= 10:
    #         return self.name
    #     else:
    #         return None


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

    @classmethod
    def instantiate_from_csv(cls, ):
        pass

    @staticmethod
    def string_to_number(number):
        pass


