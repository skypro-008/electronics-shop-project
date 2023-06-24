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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

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
    def name(self) -> str:
        """
        Геттер для атрибута name. Возвращает наименование товара
        """
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        """
        Сеттер для атрибута name. Позволяет изменить наименование товара.
        Проводит проверку длины наименования (не более 10 символов)
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            print('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        with open(os.path.join(os.path.dirname(__file__), 'items.csv'), newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(num_str: str):
        """
        Статический метод, возвращающий число из числа-строки
        """
        if '.' in num_str:
            return int(float(num_str))
        else:
            return int(num_str)
