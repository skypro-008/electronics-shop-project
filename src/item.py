import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            print("Exception: Длина наименования товара превышает 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __repr__(self):
        module_name = "__main__"
        class_name = self.__class__.__name__
        return f"<{module_name}.{class_name} object at {hex(id(all))}>"

    @classmethod
    def instantiate_from_csv(cls):
        """Открытие файла csv"""
        cls.all = []
        with open("src\items.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name = row[0]
                price = row[1]
                quantity = row[2]
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        """ Статическая функция преобразования строкового представления числа в целое число"""
        return_number = float(number)
        return int(return_number)
