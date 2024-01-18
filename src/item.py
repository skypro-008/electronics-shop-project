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

    @property
    def name(self):
        return self.__name

    @classmethod
    def instantiate_from_csv(cls,path):
        with open(path, newline='', encoding ='windows-1251') as file:
            file_csv = file.DictReader(file, delimiter=",")
            for files in file_csv:
                name = files['name']
                price = int(files['price'])
                quantity = int(files['quantity'])
                return cls(name, price, quantity)

    @staticmethod
    def string_to_number(number:str):
        return int(number)

    @name.setter
    def name_len(self, name):
        if len(self.name) <= 10:
            self.name = name
        else:
            self.name = name[:10]
        return self.name

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

    @name.setter
    def name(self, value):
        self._name = value
