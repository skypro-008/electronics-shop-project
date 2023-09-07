import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    max_name_len = 10
    pay_rate = 1.0
    all = []
    keep = True

    @classmethod
    def instantiate_from_csv(cls, filename='src/items.csv', encoding='windows-1251', delimiter=','):
        Item.all.clear()
        with open(filename, 'r', encoding=encoding) as file:
            items = csv.reader(file, delimiter=delimiter)
            next(items, None)
            for name, price, quantity in items:
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(string: str) -> int:
        return int(float(string))

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self._price = price
        self._quantity = quantity

        if Item.keep:
            Item.all.append(self)

    def __repr__(self):
        # return (f"{self.__class__.__name__}("
        #         f"name='{self.name}', "
        #         f"price={self._price}, "
        #         f"quantity={self._quantity}"
        #         ")")
        return (f"{self.__class__.__name__}("
                f"'{self.name}', "
                f"{self._price}, "
                f"{self._quantity}"
                ")")

    def __str__(self):
        return self._name

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
        self._price *= self.pay_rate

    @property
    def price(self) -> float:
        return self._price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > Item.max_name_len:
            raise Exception(f'Длина наименования товара превышает {Item.max_name_len} символов')
        self._name = value
