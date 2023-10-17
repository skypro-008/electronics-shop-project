import os.path
from csv import DictReader


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
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def verify_name(cls, name):
        """
        Имя должно быть не больше 10 символов
        """
        return name[:10]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name = self.verify_name(name)
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path_name):
        """
        Создаёт объекты из данных файла .csv
        """

        items = []
        path_name = str(cls.path_file(path_name))
        with open(path_name, newline='', encoding='windows-1251') as csv_f:
            reader = DictReader(csv_f, delimiter=',')
            for row in reader:
                name = str(row['name'])
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
            cls.all = items

    @staticmethod
    def path_file(path_name):
        """
        Создаёт путь для файла при условии, что файл лежит в другой папке родительского каталога

        :param path_name: путь к файлу в подобном формате 'src/items.csv'
        """
        path_list = path_name.split('/')
        path_file = os.path.join('..', path_list[0], path_list[1])
        return path_file

    @staticmethod
    def string_to_number(string):
        string = string.split('.')
        return int(string[0])
