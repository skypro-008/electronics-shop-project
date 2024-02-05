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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    @property
    def name(self):
        """Геттер для приватного атрибута name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Проверяет длину атрибута name, если больше 10 символов - возвращает первые 10"""
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]
        return self.__name


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
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path) -> None:
        """
        Создает экземпляры класса Item из данных в файле items.csv.
        """
        cls.all.clear()
        file_path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(file_path, 'r', newline='', encoding='cp1251') as file:
            data = csv.DictReader(file)
            for row in data:
                #print(row)
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        return int(float(string))
