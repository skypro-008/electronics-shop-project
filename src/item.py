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
        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"



    @property
    def name(self):
        """
        Метод геттер для свойства name
        """
        return self.__name


    @name.setter
    def name(self, name):
        """
        Этот метод сеттер проверяет что длина наименования товара не больше 10 симвовов.
        В противном случае, обрезает строку (оставляет первые 10 символов).
        """
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]


    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open('C:/Users/USER/PycharmProjects/electronics-shop-project/src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row.get('name'), float(row.get('price')), int(row.get('quantity')))



    @staticmethod
    def string_to_number(value: str):
        """статический метод, возвращающий число из числа-строки
        """
        return int(float(value))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_cost = self.price * self.quantity
        return total_cost

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

