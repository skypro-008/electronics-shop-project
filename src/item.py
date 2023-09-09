import csv
import pathlib


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

    def __repr__(self):
        """
        Возвращает экземпляр класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает название экземпляра класса
        """
        return f"{self.name}"

    @property
    def name(self):
        """
        Геттер для name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Проверка длинны name, которая не должна превышать 10 символов
        """
        self.__name = name[:10]

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

    def __add__(self, other):
        """
        Возвращение сложения экземпляров класса Phone и Item по количеству товара в магазине
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Phone или Item и дочерние от них.')
        return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла src/items.csv
        """
        csv_file_path = pathlib.Path(__file__).parent.resolve() / filename
        try:
            with open(csv_file_path, 'r', encoding='windows-1251') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    if name is None or price is None or quantity is None:
                        raise InstantiateCSVError
                    cls.all.append(Item(name, cls.string_to_number(price), cls.string_to_number(quantity)))
        except FileNotFoundError:
            raise NotFoundCSVError

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(string))


class LanguageMixin:
    __lang = "EN"

    def change_lang(self):
        if self.__lang == "EN":
            self.__lang = "RU"
        else:
            self.__lang = "EN"
        return self

    @property
    def language(self):
        return self.__lang


class CSVError(Exception):
    """Класс на ошибку в читаемом файле"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная ошибка в CSV файле"

    def __str__(self):
        return self.message


class InstantiateCSVError(CSVError):
    """Класс на ошибку в читаемом файле, например, отсутствует одна из колонок данных"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"


class NotFoundCSVError(CSVError):
    """Класс на проверку наличия файла"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Отсутствует файл item.csv"
