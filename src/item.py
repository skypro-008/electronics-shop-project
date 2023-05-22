import csv
import os

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

        self.__name = name  # Название товара
        self.price = price  # Цена за единицу товара.
        self.quantity = quantity  # Количество товара в магазине

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, add_name: str):
        try:
            if len(add_name) <= 10:
                self.__name = add_name

        except:
            print('Длина наименования товара превышает 10 символов')

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
        return self.price


    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Вызываем классы из файла"""

        cls.all.clear()
        csv_file = os.path.join('src', 'items.csv')
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(line):
        """метод, возвращающий число из числа-строки"""
        a = float(line)
        return int(a)




