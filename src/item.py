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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

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

    @classmethod
    def instantiate_from_csv(cls, file_items):
        cls.all = []

        with open(file_items, encoding='cp1251') as csv_file:
            file = DictReader(csv_file)

            for element in file:
                name = element['name']
                price = float(element['price'])
                quantity = int(element['quantity'])
                item = cls(name, price, quantity)
                item.name = name
                item.price = price
                item.quantity = quantity
                cls.all.append(item)

    @staticmethod
    def string_to_number(str_num):
        return int(float(str_num))
