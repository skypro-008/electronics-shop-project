import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.
    all = []

    # path = os.path.join('..', 'electronics-shop-project_AV', 'scr', 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.verify_name(name)

        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.all.append(self)

    @classmethod
    def verify_name(cls, name):
        """Проверяет, что длина наименования товара не больше 10 символов"""
        if len(name) >= 10:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open('../src/items.csv', encoding='utf-8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all = [cls((row['name']), float(row['price']), int(row['quantity'])) for row in reader]
        return cls.all

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.verify_name(name)
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        :return:  стоимость товара с скидкой.
        """
        self.price *= self.pay_rate
        return self.pay_rate

