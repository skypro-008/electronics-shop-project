import csv
import os.path


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
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, ):
        """
        Считываем файл и инициализируем экземпляры класса

        """
        items = []
        with open('/home/renat/PycharmProjects/electronics-shop-project/src/items.csv', 'r',
                  encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            next(reader)
            for data in reader:
                item = Item(data['name'], float(data['price']), int(data['quantity']))
                items.append(item)
            return items

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Преобразуем число из строки
        """
        return int(number.split(".")[0])

    @property
    def personal_name(self):
        """
        Геттер для названия товара
        """
        return self.__name

    @personal_name.setter
    def name(self, value):
        """
        Сеттер для названия товара
        """
        if len(value) < 10:
            #     raise ValueError("Personal name is too long")
            # self.personal_name = value
            self.__name = value
        else:
            print("Name mast be no more than 10 characters long.")
 #raise ValueError("Name mast be no more than 10 characters long.")