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
        if type(name) is str:
            self.name = name
        else:
            raise ValueError("Наименование должно быть строкой")

        if type(price) is float:
            self.price = price
        elif type(price) is int:
            self.price = float(price)
        else:
            raise ValueError("Цена должна быть числом")

        if type(quantity) is int:
            self.quantity = quantity
        else:
            raise ValueError("Количество должно быть выражено целым числом")

        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        if not isinstance(self.price, (int, float)):
            raise ValueError("Цена задана неверно!")
        elif not isinstance(self.quantity, int):
            raise ValueError("Количество задано неверно!")
        else:
            return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        if not isinstance(self.price, (int, float)):
            raise ValueError("Цена задана неверно!")
        elif not isinstance(self.pay_rate, float):
            raise ValueError("Размер скидки задан неверно!")
        elif self.pay_rate > 1:
            raise ValueError("Размер скидки задан неверно!")
        else:
            self.price *= self.pay_rate