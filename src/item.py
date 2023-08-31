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
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        """
        присваивает название товара если его длина менее 10 символов
        :name_: название товара
        """
        if len(self.__name) < 10:
            self.__name = name_
        else:
            self.__name = self.__name[0:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        открывает csv файл и создает на их основе экземпляры класса
        :path: путь к файлу
        """
        Item.all = []
        with open(path, "r") as file:
            file_reader = csv.DictReader(file)
            for product in file_reader:
                cls(product["name"], float(product["price"]), int(product["quantity"]))

    @staticmethod
    def string_to_number(string_number):
        """
        меняет тип данных из str в int
        :string_number:число-строка
        """
        return int(float(string_number))
