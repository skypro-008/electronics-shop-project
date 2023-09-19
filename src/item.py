import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if len(name) > 10:
            return f'{name[0:10]}'
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self, discount: float) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= discount

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла.
        :param filename: Имя файла.
        :return: None
        """

        with open('../src/items.csv', newline='', encoding='windows-1251') as csvfile:
            csv_dict = csv.DictReader(csvfile, delimiter=',')
            for row in csv_dict:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                item = cls(name, price, quantity)


    @staticmethod
    def string_to_number(string_value: str) -> float:
        return float(string_value)