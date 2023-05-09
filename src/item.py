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

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        try:
            if len(name) <= 10:
                self.__name: str = name
        except:
            raise Exception("Длина наименования превышает 10 симвовов")



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> list:
        cls.all = []
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(ROOT_DIR, 'items.csv'), newline='') as file:
            rows = csv.DictReader(file)
            for row in rows:
                name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                item = cls(name, price, quantity)
                cls.all.append(item)
        # проверяем уникальность имен и оставляем только уникальные комбинации имя: ключ и преобразует экземпляры классов(ключи) в список
        cls.all = list({item.name: item for item in cls.all}.values())
        return cls.all



    @staticmethod
    def string_to_number(string: str) -> int:
        if "." in string:
            number = int(float(string))

        else:
            number = int(string)
        return number



