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
        self.__name = None
        self.price = price
        self.quantity = quantity
        self.name = name
        Item.all.append(self)

    def __repr__(self):
        """Возвращает данные для разработчика"""
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает данные для пользователя"""
        return self.__name

    @property
    def name(self):
        """Возвращает приватную __name"""
        return self.__name

    @name.setter
    def name(self, string):
        """Получает string и записывает в __name, проверяя длину string"""
        if len(string) < 11:
            self.__name = string
        else:
            print('Длина наименования товара не больше 10 символов')

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

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []

        with open('../src/items.csv', newline='', encoding="cp1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        try:
            number = int(string)
        except ValueError:
            try:
                number = int(float(string))
            except ValueError:
                number = None
        return number
