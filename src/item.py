import csv
from csv import DictReader


class InstantiateCSVError(Exception):
    """
    Класс исключения если файл item.csv поврежден или его нет
    """

    def __init__(self, *args):
        self.message = args[0] if args else "InstantiateCSVError: файл item.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return int(self.quantity) + int(other.quantity)
        raise ValueError("Складывать можно только экземпляры классов Item и Phone")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception("Длина названия больше 10 символов")

    @classmethod
    def instantiate_csv(cls, path_to_file) -> None:
        """
        Класс-метод, инициирующий экземпляры класса из файла .csv
        """

        cls.all.clear()

        with open(path_to_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                cls(line['name'], line['price'], line['quantity'])

                if not line['name'] or not line['price'] or not line['quantity']:
                    raise InstantiateCSVError
            if len(cls.all) < 5:
                raise InstantiateCSVError

    @classmethod
    def instantiate_from_csv(cls) -> None:

        '''
        Класс-метод для отлова ошибок при инициализации экземпляров класса из файла .csv
        '''
        path_to_file = '../src/items.csv'
        try:
            cls.instantiate_csv(path_to_file)
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(line):
        numb = int(float(line))
        return numb

    def calculate_total_price(self):

        return self.price * self.quantity

    def apply_discount(self):

        self.price *= self.pay_rate