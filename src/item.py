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
        return f'Item({self.__name}, {self.price}, {self.quantity})'

    @property
    def name(self):
        """геттер атрибута name"""

        return self.__name

    @name.setter
    def name(self, name):
        """сеттер атрибута name"""

        if 0 < len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_path: str):
        """метод создания экземпляров класса из файла items.csv"""

        cls.all = []
        with open(csv_path, 'rt', newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row["name"], row["price"], row["quantity"])

    @staticmethod
    def string_to_number(string_num):
        """возвращает целое число из строки"""

        if isinstance(string_num, str):
            return round(float(string_num.split('.')[0]))
        else:
            print('Данная запись не является числом-строкой')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate
