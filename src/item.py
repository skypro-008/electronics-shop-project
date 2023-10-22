import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "Файл item.csv поврежден"


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
        self._name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self._name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            return ValueError
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        result = self.quantity * self.price
        return result

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    @property
    def name(self):
        """ Добавление getter к name"""
        return self._name

    @name.setter
    def name(self, name):
        """Добавление setter к name и проверка длины"""
        self._name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open('../items.csv', encoding='cp1251') as file: #менял путь к файлу для вызова исключения FileNotFoundError
                read = csv.DictReader(file)
                for x in read:
                    name = x["name"]
                    price = x["price"]
                    quantity = x["quantity"] #None для вызова исключения InstantiateCSVError
                    if name is None or price is None or quantity is None:
                        raise InstantiateCSVError
                    item = cls(name, price, quantity)
                    cls.all.append(item)
        except FileNotFoundError:
            print("Отсутствует файл items.csv")
        except InstantiateCSVError as m:
            print(m.message)

    @staticmethod
    def string_to_number(string: str):
        x = float(string)
        return int(x)