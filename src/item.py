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
    def name(self, value):
        if len(value) > 10:
            print("Длина наименования товара превышает 10 символов.")
            self.__name = value[:10]
        else:
            self.__name = value

    @staticmethod
    def instantiate_from_csv():
        """
        Создание экземпляра класса item из csv-файла.
        """
        with open('../src/items.csv', "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                Item.all.append(row)

    @staticmethod
    def string_to_number(string):
        return int(string)
