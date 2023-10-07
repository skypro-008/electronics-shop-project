import csv

word_csv = []


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[0:10]


    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        cls.all.clear()
        with open(filename, encoding="UTF-8", errors='replace') as file:
            words = csv.DictReader(file)
            # items = []
            for word in words:
                name = word["name"]
                price = float(word["price"])
                quantity = int(word["quantity"])
                cls(name, price, quantity)



    @staticmethod
    def string_to_number(str_number: str) -> int:
        number = str_number.split('.')
        return int(number[0])
