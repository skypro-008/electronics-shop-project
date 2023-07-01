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
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if len(self.__name) > 10:
            raise ValueError('Длинна товара превышает 10 символов')
        else:
            self.__name = name[:10]



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:/Users/Ruslan/PycharmProjects/electronics-shop-project/src/items.csv ', 'r', newline='') as cvsfile:
            cls.all = []
            reader = csv.DictReader(cvsfile)
            for row in reader:
                cls.__name = row['name']
                cls.price = float(row['price'])
                cls.quantity = int(row['quantity'])
                item = Item(name, price, quantity)
                cls.all.append(item)
            print(cls.all)

    @staticmethod
    def string_to_number(stroka):
        return int(''.join(filter(str.isdigit, stroka)))



