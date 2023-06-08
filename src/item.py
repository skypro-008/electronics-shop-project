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
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_length):
        """
        Проверяем что длина наименования товара не больше 10 символов
        """
        if len(name_length) < 10:
            self.__name = name_length
        else:
            print("Exception: Длина наименования товара превышает 10 символов")
            # raise Exception('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        file = '../src/items.csv'
        cls.all.clear()
        with open(file, newline="") as csvfile:
            item = csv.DictReader(csvfile)
            for row in item:
                cls(row['name'], row['price'], row["quantity"])

    @staticmethod
    def string_to_number(file):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(file))
