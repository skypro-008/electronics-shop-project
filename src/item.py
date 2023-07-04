from csv import DictReader


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

    @classmethod
    def instantiate_from_csv(cls):
        # читаем CSV файл как список словарей, ключи
        # которого заданы первой строкой файла 'names.csv'
        with open('../src/items.csv', 'r', encoding='windows-1251') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), cls.string_to_number(row['quantity']))


    @staticmethod
    def string_to_number(str_number: str):
        """возвращает число из числа-строки"""
        return int(float(str_number))

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if type(value) is not str:
            raise TypeError('name must be a string')
        elif len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]

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
