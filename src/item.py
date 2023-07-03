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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.pay_rate * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) > 10:
            raise Exception('Наименования товара должно быть не больше 10 символов')
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file_path='items.csv'):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        items = []
        try:
            with open(os.path.join(os.path.dirname(__file__), file_path), newline='', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['name']
                    price = int(row['price'])
                    quantity = int(row['quantity'])
                    item = cls(name, price, quantity)
                    items.append(item)
                    cls.all.append(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except ValueError:
            raise InstantiateCSVError("Файл item.csv поврежден")
        return items

    @staticmethod
    def string_to_number(value):
        """
        Статический метод, возвращающий число из числа-строки.
        """
        return int(float(value))

    def __add__(self, other):
        """
        Сложения экземпляров класса Phone и Item.
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return 'Не экземпляр класса Item'


class InstantiateCSVError(Exception):
    """
    Класс-исключение, возникающее при некорректных данных в файле items.csv
    """
    def __init__(self, message="Файл item.csv поврежден"):
        super().__init__(message)
        self.message = message



# print(Item.instantiate_from_csv())
# print(Item.instantiate_from_csv('item.csv'))
