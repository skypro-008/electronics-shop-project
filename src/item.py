import csv


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
        self.all.append(self)

    @property
    def name(self):
        """
        Геттер названия товара
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Сеттер названия товара
        """
        if len(new_name) > 10:
            self.__name = new_name[0:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, data):
        """
        Класс-метод, инициализирующий экземпляры класса Item
        param name: Название товара.
        param price: Цена за единицу товара.
        param quantity: Количество товара в магазине.
        """
        cls.all.clear()
        with open(f"D:/Milyaev/leesons/electronics-shop-project/{data}", newline='') as csvfile:
            content = csv.DictReader(csvfile)

            for row in content:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string_namber):
        """
        Статический метод перевода числа из строкового значения в числовое

        :return: Числовое значение
        """
        return int(float(string_namber))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

##############################