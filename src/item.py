import math
import csv

CSV_FILE = '..\\src\\1.csv'


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
        self.__name = ""
        self.name = name.strip()
        if not (isinstance(price, float) or isinstance(price, int)):
            raise ValueError('Цена за единицу товара должна быть только числом.')
        if price <= 0:
            raise ValueError('Цена за единицу товара может быть положительным числом!')
        self.price = price
        if not isinstance(quantity, int):
            raise ValueError('Количество товара должно быть только числом.')
        if quantity <= 0:
            raise ValueError('Количество товара может быть только положительным числом"')
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
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            value = value[:10]
        self.__name = value

    @staticmethod
    def string_to_number(value: str) -> int:
        float_value = float(value)
        return math.floor(float_value)

    @classmethod
    def instantiate_from_csv(cls):
        # Обнуляем список объектов класса
        cls.all = []
        with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item(row.get('name'), float(row.get('price')), int(row.get('quantity')))


if __name__ == "__main__":
    print(Item.string_to_number('5.9'))
    print(Item.string_to_number('5'))
    print(Item.string_to_number('5.0'))

    Item.instantiate_from_csv()
    print(len(Item.all))
    print(Item.all[0].name)
