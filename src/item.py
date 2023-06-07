import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла items.csv.
        """
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'items.csv'),
                  'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)
            for item_position in reader:
                name = item_position['name']
                price = float(item_position['price'])
                quantity = int(item_position['quantity'])
                item = Item(name, price, quantity)
                cls.all.append(item)

# Добавим статический метод string_to_number(), возвращающий число из числа-строки.

    @staticmethod
    def string_to_number(namber):
        return int(float(namber))

    def __repr__(self):
        """
        Возвращает строковое представление экземпляров класса Item.
        """
        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"

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

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = (self.price * self.quantity)
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, add_name: str):
        if len(add_name) >= 10:
            raise ValueError('Длина наименования товара превышает 10 символов')
        else:
            self.__name = add_name
