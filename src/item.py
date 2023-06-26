import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: int, quantity: int):
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

    # def __call__(self, stc):
    #     return Item.all

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception("Наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open("../src/items.csv", encoding='utf-8') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=",")
            for item in file_reader:
                cls(item["name"],
                    item["price"],
                    item["quantity"])

    @staticmethod
    def string_to_number(string: str):
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        price_global = self.price * self.quantity
        return price_global

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        make_discount = self.price * self.pay_rate
        return make_discount
