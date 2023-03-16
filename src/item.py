import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @staticmethod
    def string_to_number(str_num: str):
        try:
            return int(float(str_num))
        except:
            return 'Введено некорректное значение'

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        with open('../src/items.csv', newline='') as f:
            for row in csv.DictReader(f):
                cls(row['name'], row['price'], row['quantity'])

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
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            print('Длина наименования товара превышает 10 символов.')
            # raise Exception('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = new_name

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
