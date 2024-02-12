import csv

from settings import NAME_DIR


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

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            # print("Длина наименования товара превышает 10 символов")
            self.__name = name[:10]
        else:
            self.__name = name

    @property
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

    @classmethod
    def instantiate_from_csv(cls):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        with open(NAME_DIR, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row['name'], row['price'], row['quantity'])
                name = row['name']
                price = row['price']
                quantity = row["quantity"]
                cls(name, price, quantity)
            return cls

    @staticmethod
    def string_to_number(x):
        """
        возвращающий число из числа-строки
        """
        return int(float(x))


if __name__ == '__main__':
    pass

