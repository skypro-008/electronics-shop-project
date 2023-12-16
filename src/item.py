import csv
import os

path = os.path.join('..', 'src', 'item.csv')  # путь к файлу


class InstantiateCSVError(Exception):
    def __init__(self, message, base_message=None):
        self.base_message = base_message
        self.message = message

    def __str__(self):
        if self.base_message is None:
            return self.base_message

        return f'{self.message} - {str(self.base_message)}'


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
        self.__name = name
        if len(self.__name) > 10:
            self.__name = self.__name[:11]

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        try:
            with open(path, encoding='windows-1251', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all = [cls((row['name']), float(row['price']), int(row['quantity'])) for row in reader]
        except FileNotFoundError:
            print('_Отсутствует файл item.csv_')
        except KeyError as e:
            print(InstantiateCSVError('_Файл item.csv поврежден_', e))

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self, pay_rate=None) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return pay_rate

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"{__class__.__name__}('{str(self.__name)}', {str(self.price)}, {str(self.quantity)})"

    def __add__(self, other):
        """Метод сложения количества телефонов класса Item и его наследников"""
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только экземпляры Item и Phone')
        return self.quantity + other.quantity


    # @classmethod
    # def instantiate_from_csv(cls):
    #     cls.all.clear = []
    #     try:
    #         with open(path, encoding='windows-1251', newline='') as csvfile:
    #             items = csv.DictReader(csvfile, delimitrer=",")
    #             header = next(items)
    #             if 'name' not in header or 'price' not in header or 'quantity' not in header:
    #                 raise csv.Error('Отсутствует необходимая колона в заголовке файла CSV')
    #             else:
    #                 for item in items:
    #                     name = item["name"]
    #                     price = float(item["price"])
    #                     quantity = cls.string_to_number(item["quantity"])
    #                     cls(name, price, quantity)
    #                     print(name, price, quantity )
    #     except FileNotFoundError:
    #         print('_Отсутствует файл item.csv_')
    #     except csv.Error:
    #         print('_Файл item.csv поврежден_')
