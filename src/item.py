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
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                _name = row['name']
                price = row['price']
                quantity = int(row['quantity'])
                item = cls(_name, price, quantity)
                return item

    @staticmethod
    def string_to_number(string):
        return int(float((string)))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self._name = name[:10]
            print(self._name)
        else:
            self._name = name
            print(self._name)


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

        return self.price

#
