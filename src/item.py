import csv
from typing import Any


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all: list = []

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

    def __repr__(self) -> str:
        """
        Предоставляет информацию об объекте для разработчика.
        """
        return f"{self.__class__.__name__}{self.__name, self.price, self.quantity}"

    def __str__(self) -> str:
        """
        Предоставляет информацию о классе для пользователя.
        """
        return self.__name

    @property
    def get_name(self) -> str:
        """
        Возвращает значение атрибута '__name'.
        """
        return self.__name

    @get_name.setter
    def get_name(self, name: str) -> None:
        """
        Записывает атрибут '__name' не длиннее 10 символов.
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

    @classmethod
    def instantiate_from_csv(cls, path_file: str) -> None:
        """
        Инициализирует экземпляры класса `Item` данными из файла csv.
        """
        # Получение данных из файла и преобразование их в list(dict).
        with open(path_file, "r") as file:
            reader = csv.DictReader(file)
            items = list(reader)

            # Инициализация экземпляров класса.
            for item in items:
                name = item["name"]
                price = float(item["price"])
                quantity = int(item["quantity"])
                cls(name, price, quantity).get_name = name

    @staticmethod
    def string_to_number(data: str) -> int:
        """Возвращает число из строки."""
        return int(float(data))

    def __add__(self, other: Any) -> Any:
        """
        Складывает количество товара у экземпляров классов 'Item' и 'Phone'.
        """
        if isinstance(other, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError("Эти данные нельзя сложить.")
