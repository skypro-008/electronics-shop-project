import csv

filename = "../src/items.csv"

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
        self.pay_rate = Item.pay_rate
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
        self.price *= Item.pay_rate

    # Геттер для name
    @property
    def name(self):
        """Возвращает наименование товара. К атрибуту можно обращаться без вызова."""
        return self.__name

    # Cеттер для name
    @name.setter
    def name(self, name):
        """Сеттер проверяет, что длина наименования товара не больше 10 символов."""
        self.__name = name
        if len(name) <= 10:
            print(name)
        else:
            print("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        with open(filename, encoding='cp1251') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=",")
            for row in file_reader:
                cls(row["name"], (row["price"]), (row["quantity"]))
                cls.all.append(row["name"])
            return cls.all

    @staticmethod
    def string_to_number(str_number):
        number = float(str_number)
        number = int(number)
        return number

print(Item.all)


