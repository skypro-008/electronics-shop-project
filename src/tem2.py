import csv
import os

PATH = os.path.abspath('..')
PATH_TO_FILE = os.path.join(PATH, 'src', 'items.csv')
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
               Создание экземпляра класса item.

               :param name: Название товара.
               :param price: Цена за единицу товара.
               :param quantity: Количество товара в магазине.
               """
        self.__name = name
        self.price = price * self.pay_rate
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        with open(PATH_TO_FILE, 'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            lists = [cls(i['name'], i['price'], i['quantity']) for i in reader]
            return lists

    @staticmethod
    def string_to_number(number):
        if '.' in number:
            return int(float(number))
        elif number.isdigit():
            return int(number)

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

#item = Item('Смартфон', 10000, 5)
#print(item.name)
#item.name = 'Суперсмартфон'
#print(item.name)
#print(Item.instantiate_from_csv())
# print(Item.string_to_number('5.5'))
# print(len(Item.all))
# print(Item.all)
# print(Item.all[0])
#item1 = Item.all[0]
#print(item1.name)
