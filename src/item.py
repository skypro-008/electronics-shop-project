import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(str(self))
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

    def calculate_total_price(self) -> float:
        total = self.price * self.quantity
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        #Item.all.append(total)
        return total

    def apply_discount(self) -> None:
        self.price *= Item.pay_rate
        return self.price

    """
    Применяет установленную скидку для конкретного товара.       
    """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name
            print(name)
        #else:
            #raise ValueError('Ошибка: в наименовании товара больше 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            pass

    @staticmethod
    def string_to_number(num):
        return float(num)




item = Item('Телефон', 10000, 5)
item.name = 'СуперСмартфон'
print(item.name)
print(Item.instantiate_from_csv())