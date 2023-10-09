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
        self.item_name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

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
        self.price = round(self.price * Item.pay_rate, 2)

    @property
    def name(self):
        ''' Имя getter '''
        return self.item_name

    @name.setter
    def name(self, name):
        ''' Имя сеттер '''
        if len(name) > 10:
            self.item_name = name[:10]
        else:
            self.item_name = name

    @classmethod
    def instantiate_from_csv(cls, filename):
        ''' Создать объекты из CSV файла '''
        Item.all.clear()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.split(current_dir)[0]
        filepath = os.path.join(root_dir, filename)
        if os.path.isfile(filepath):
            with open(filepath, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_item = cls(name=row.get('name'),
                                   price=row.get('price'),
                                   quantity=row.get('quantity'))

    @staticmethod
    def string_to_number(number):
        ''' Конвертировать строку в номер '''
        rnumber = number.replace('.', '', 1).isdigit()
        if rnumber:
            onumber = float(number)
            return int(onumber)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name
