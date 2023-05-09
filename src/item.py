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
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            raise Exception(f"Длина наименования товара превышает 10 символов.")
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, csv_path='../src/items.csv'):
        cls.all = []
        with open(csv_path) as file_items:
            items = csv.DictReader(file_items, delimiter=',')
            [cls(row['name'], row['price'], row['quantity']) for row in items]

    @staticmethod
    def string_to_number(str_num: str) -> int:
        return int(float(str_num))

    def __str__(self):
        """
        Вывод данные именования по товару
        """
        return f"{self.name}"
