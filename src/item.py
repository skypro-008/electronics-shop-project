import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
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

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """Функция проверяет длину наименования товара, чтобы было не более 10 символов"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        """
        Создает экземпляры класса Item из данных в файле items.csv
        """
        cls.all = []
        with open(path, 'r', encoding='windows-1251') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            for row in rows:
                Item(str(row['name']), float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(str_number):
        """Возвращает число из числа-строки"""
        number = float(str_number)
        return int(number)
