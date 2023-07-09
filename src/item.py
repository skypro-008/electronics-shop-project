import csv

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
        return self.__name


    @name.setter
    def name(self, new_name: str):
        """
        В сеттере `name` осуществляется проверка длины наименования товара.
        Допускается наименование не больше 10 симвовов, в противном случае,
        строка обрезается (остаются первые 10 символов)
        """
        self.__name = new_name
        if len(list(self.__name)) > 10:
            self.__name = str("".join(list(self.__name)[:10]))
        else:
            self.__name = new_name


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
        self.price = self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv
        """
        items_csv = 'C:/Users/user/PycharmProjects/electronics-shop-project/src/items.csv'
        with open(items_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            Item.all = []
            for row in reader:
                name = Item.check_to_str(row['name'])
                price = Item.check_to_float(row['price'])
                quantity = Item.check_to_int(row['quantity'])
                item = Item(name, price, quantity)
                item.name = name


    @staticmethod
    def string_to_number(number: str):
        """Cтатический метод, возвращающий число из числа-строки"""
        if type(float(number)) == float:
            return int(float(number))
        else:
            print("String must be digit")


    @staticmethod
    def check_to_str(value):
        """Cтатический метод, возвращающий str"""
        if isinstance(value, str):
            value_str = value
        else:
            value_str = str(value)
        return value_str


    @staticmethod
    def check_to_float(value):
        """Cтатический метод, возвращающий float"""
        if isinstance(value, float):
            value_float = value
        else:
            value_float = float(value)
        return value_float


    @staticmethod
    def check_to_int(value):
        """Cтатический метод, возвращающий int"""
        if isinstance(value, int):
            value_int = value
        else:
            value_int = int(float(value))
        return value_int
